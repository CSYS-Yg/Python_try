import requests
from bs4 import BeautifulSoup
import re
import imghdr
import base64

import getContent
import newEpubStructure

id = '62218d1d8f42aea18e84d345e0e6923d'


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
    newEpubStructure.newNcx(refiningData)
    newEpubStructure.newOpf(refiningData)
    # 批量请求接口获取数据
    for i in refiningData:
        content = getContent.getText(i['url'])
        content = content.json()
        # 美化拿到的数据
        htmlContent = BeautifulSoup(content['content'], 'html.parser')
        # 图片下载替换处理
        contentImage(htmlContent, i["title"], i["number"])


# 读取文本内容
def contentRefining(htmlContent, name, index):
    paraData = htmlContent.find_all('para')
    contentsList = []
    contentsList.append("<title>" + name.split('丨')[1] + "</title>")
    for i in paraData:
        lineContents = i.contents[1].string
        if lineContents:
            if (lineContents.find('isImg~') != -1):
                img = lineContents.split("~")[1]
                contentsList.append('<img src="../img/' + img + '" />')
            else:
                bgcolor = ""
                if (len(i.contents[2].find_all('back-color')) > 0):
                    bgcolor = i.contents[2].find_all('back-color')[0].find_all(
                        'value')[0].string
                # fontSize = i.contents[2].find_all('font-size')[0].find_all(
                #     'value')[0].string
                color = i.contents[2].find_all('color')[0].find_all(
                    'value')[0].string
                bold = False
                boldList = i.contents[2].find_all('bold')
                if len(boldList):
                    bold = True
                if bold and color == "#ff6622":
                    contentsList.append('<p class="sub-title red-content">' +
                                        lineContents + '</p>')
                elif bold and color == "#545454":
                    contentsList.append('<p class="main-content fw-b">' +
                                        lineContents + '</p>')
                elif bgcolor == "#f7dad5":
                    contentsList.append(
                        '<p class="main-content gray-content">' +
                        lineContents + '</p>')
                else:
                    contentsList.append('<p class="main-content">' +
                                        lineContents + '</p>')
    newEpubStructure.newHtml(contentsList, index)


# 匹配图片
def contentImage(htmlContent, name, index):
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
        newEpubStructure.newImg(content, imgname)
        imgname = '<para><coid></coid><text>isImg~' + imgname + '</text></para>'  # noqa
        text = text.replace(imageList[i], imgname)
    text = BeautifulSoup(text, 'html.parser')
    contentRefining(text, name, index)


# 获取编号 Id
def getNumbering(number):
    content = "0000000" + str(number)
    return content[-5:]
