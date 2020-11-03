import requests
from bs4 import BeautifulSoup
import re
import imghdr
import base64

import getContent
import newEpubStructure

id = '62218d1d8f42aea18e84d345e0e6923d'

isImgEncrypt = False


# 数据处理
def refining(url):
    # 获取数据
    data = getContent.getData(url)
    data = data[2]

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
    # 列表排序
    refiningData.sort(key=lambda x: x["number"])
    # 根据列表生成 ncx 文件
    newEpubStructure.newNcx(refiningData)
    # 根据列表生成 opf 文件
    newEpubStructure.newOpf(refiningData)
    # 批量请求接口获取数据
    for i in refiningData:
        content = getContent.getText(i['url'])
        content = content.json()
        # 美化拿到的数据
        htmlContent = BeautifulSoup(content['content'], 'html.parser')
        # 图片下载，并进行相关图片或 base64 数据进行文本替换处理
        name = i["title"].split('丨')[1].replace('.note', '')
        contentImage(htmlContent, name, i["number"])


# 匹配图片
def contentImage(htmlContent, name, index):
    # 图片列表
    text = str(htmlContent)
    # 找出图片集合
    imageList = re.findall('<source/>(.*?)<', str(htmlContent))
    for i in range(len(imageList)):
        typeName = ''
        # 图片类型判断
        if (imageList[i].find('base64,') == -1):
            data = requests.get(imageList[i])
            content = data.content
            typeName = imghdr.what(None, content)
        else:
            content = imageList[i].replace('data:image/gif;base64,', '')
            content = base64.b64decode(content)
            typeName = imghdr.what(None, content)
        if (isImgEncrypt):
            imgname = str(index) + '_' + str(i) + '.' + typeName
        else:
            imgname = name + '_' + str(i) + '.' + typeName
        newEpubStructure.newImg(content, imgname)
        # 替换成指定文本内容
        imgname = '<para><coid></coid><text>isImg~' + imgname + '</text></para>'  # noqa
        text = text.replace(imageList[i], imgname)
    text = BeautifulSoup(text, 'html.parser')
    # 对替换后的文本，进行数据分类，添加不同样式
    contentRefining(text, name, index)


# 数据分类，添加不同样式
def contentRefining(htmlContent, name, index):
    paraData = htmlContent.find_all('para')
    contentsList = []
    contentsList.append("<title>" + name + "</title>")
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
    # 对处理好的内容，生成 html
    newEpubStructure.newHtml(contentsList, index)


# 获取编号 Id,返回 5 位长度
def getNumbering(number):
    content = "0000000" + str(number)
    return content[-5:]
