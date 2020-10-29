import requests
from bs4 import BeautifulSoup
import re
import os
import imghdr
import base64

import getContent

id = '62218d1d8f42aea18e84d345e0e6923d'

imgPath = 'E:\github_project\epub-book\kexuezhandouzhinan\OEBPS\img\/'
HtmlPath = 'E:\github_project\epub-book\kexuezhandouzhinan\OEBPS\content\/'


# 请求接口，获取列表数据
def getData(url):
    data = requests.get(url)
    dataJson = data.json()
    refining(dataJson[2])


# 数据处理
def refining(data):
    refiningData = []
    for i in data:
        purl = i['p'].split('/', 2)[2]
        purl = 'https://note.youdao.com/yws/public/note/' + id + '/' + purl
        number = i['tl'].split('丨')[0]
        refiningData.append({
            "title": i['tl'],
            "number": int(number),
            "url": purl,
        })
    refiningData.sort(key=lambda x: x["number"])
    # 批量请求接口获取数据
    content = getContent.getText(refiningData)
    content = content.json()
    # 美化拿到的数据
    htmlContent = BeautifulSoup(content['content'], 'html.parser')
    # 图片下载替换处理
    contentImage(htmlContent, content['tl'])


# 读取文本内容
def contentRefining(htmlContent):
    paraData = htmlContent.find_all('para')
    for i in paraData:
        lineContents = i.contents[1].string
        if lineContents:
            if (lineContents.find('isImg~') != -1):
                print('img:' + lineContents)
            else:
                bgcolor = i.contents[2].find_all('back-color')[0].find_all(
                    'value')[0].string
                fontSize = i.contents[2].find_all('font-size')[0].find_all(
                    'value')[0].string
                color = i.contents[2].find_all('color')[0].find_all(
                    'value')[0].string
                bold = False
                boldList = i.contents[2].find_all('bold')
                if len(boldList):
                    bold = True
                print(bgcolor, fontSize, color, bold, lineContents)

    # for i in paraData:
    #     if x == 1:
    #         if
    #         print(i.contents[2].find_all('back-color')[0].find_all('value')
    #               [0].string)
    #         x = x + 1


# 匹配图片
def contentImage(htmlContent, name):
    # 图片列表
    text = str(htmlContent)
    imageList = re.findall('<source/>(.*?)<', str(htmlContent))
    for i in range(len(imageList)):
        typeName = ''
        if (imageList[i].find('base64,') == -1):
            data = requests.get(imageList[i])
            content = data.content
            typeName = imghdr.what(None, content)
        else:
            content = imageList[i].replace('data:image/gif;base64,', '')
            content = base64.b64decode(content)
            typeName = imghdr.what(None, content)
        imgname = name + '_' + str(i) + '.' + typeName
        if not os.path.exists(os.path.split(imgPath)[0]):
            os.makedirs(os.path.split(imgPath)[0])
        with open(imgPath + imgname, 'wb') as fileName:
            fileName.write(content)
            fileName.close()
        imgname = '<para><coid></coid><text>isImg~' + imgname + '</text></para>'  # noqa
        text = text.replace(imageList[i], imgname)
    text = BeautifulSoup(text, 'html.parser')
    contentRefining(text)
    # # 美化数据，新增页面
    # text = text.prettify()
    # newFile(name, text)


# # 打开文件，重新写入，或直接新建文件
def newFile(name, content):
    with open(name + '.html', 'w', encoding='utf-8') as contentHtml:
        contentHtml.write(content)
        contentHtml.close()
