import requests
from bs4 import BeautifulSoup
import re
import imghdr
import base64

import getContent
import newEpubStructure

id = 'e2574ee5dd46d31b7a500a57961b9b72'

isImgEncrypt = True


# 数据处理
def refining(url):
    # 获取数据
    data = getContent.getData(url)
    data = data[2]

    refiningData = []
    for i in data:
        purl = i['p'].split('/', 2)[2]
        purl = 'https://note.youdao.com/yws/public/note/' + id + '/' + purl
        number = re.findall('第 (.*?) 讲', i['tl'])[0]
        refiningData.append({
            "title": i['tl'].replace('.note', ''),
            "number": int(number),
            "url": purl,
        })
    # 列表排序
    refiningData.sort(key=lambda x: x["number"])
    # # 根据列表生成 ncx 文件
    newEpubStructure.newNcx(refiningData)
    # # 根据列表生成 opf 文件
    newEpubStructure.newOpf(refiningData)
    # 批量请求接口获取数据
    for i in refiningData:
        # if (i["number"] == 1):
        content = getContent.getText(i['url'])
        content = content.json()
        # 美化拿到的数据
        htmlContent = BeautifulSoup(content['content'], 'html.parser')
        contentRefining(htmlContent, i["title"], i["number"])


# 数据分类，添加不同样式
def contentRefining(htmlContent, name, index):
    paraData = htmlContent.find_all('para')
    contentsList = []
    contentsList.append("<title>" + name + "</title>")
    contentsList.append('<h1 class="main-title">' + name + '</h1>')
    for i in paraData:
        lineContents = i.contents[1].string
        if lineContents:
            # bgcolor = ""
            # if (len(i.contents[2].find_all('back-color')) > 0):
            #     bgcolor = i.contents[2].find_all('back-color')[0].find_all(
            #         'value')[0].string
            # fontSize = i.contents[2].find_all('font-size')[0].find_all(
            #     'value')[0].string
            color = ''
            if (len(i.contents[2].find_all('color')) > 0):
                color = i.contents[2].find_all('color')[0].find_all(
                    'value')[0].string
            bold = False
            boldList = i.contents[2].find_all('bold')
            if len(boldList):
                bold = True
            if (bold and color == '') or (bold and color == '#0e0d0d'):
                contentsList.append('<p class="first-level-title">' +
                                    lineContents + '</p>')
            elif bold and (color == "#ffc000" or color == "#ffca00"):
                contentsList.append('<p class="tag-content-yellow">' +
                                    lineContents + '</p>')
            elif bold and color == "#414040":
                contentsList.append('<p class="main-content-bold">' +
                                    lineContents + '</p>')
            else:
                contentsList.append('<p class="main-content">' + lineContents +
                                    '</p>')
    # 对处理好的内容，生成 html
    newEpubStructure.newHtml(contentsList, index)


# 获取编号 Id,返回 5 位长度
def getNumbering(number):
    content = "0000000" + str(number)
    return content[-5:]
