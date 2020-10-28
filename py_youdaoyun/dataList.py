import requests
from bs4 import BeautifulSoup
import re
import os
import imghdr
import base64

import getContent

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
        refiningData.append({
            "title": i['tl'],
            "url": purl,
        })
    # 批量请求接口获取数据
    content = getContent.getText(refiningData)
    content = content.json()
    # 美化拿到的数据
    htmlContent = BeautifulSoup(content['content'], 'html.parser')
    # contentRefining(htmlContent)
    contentImage(htmlContent, content['tl'])


# 读取文本内容
def contentRefining(htmlContent):
    paraData = htmlContent.find_all('para')
    for i in paraData:
        if (i.contents[1].string):
            print(i.contents[1].string)


# 匹配图片
def contentImage(htmlContent, name):
    # 图片列表
    text = str(htmlContent)
    imageList = re.findall('<source/>(.*?)<', str(htmlContent))
    for i in range(len(imageList)):
        x = '<para><text>' + 'img' + str(i) + 'img' + '</text></para>'
        text = text.replace(imageList[i], x)
        if (imageList[i].find('base64,') == -1):
            urlDownload(imageList[i], i)
        else:
            baseDownload(imageList[i], i)
    text = BeautifulSoup(text, 'html.parser')
    text = text.prettify()
    # 数据写入，新增页面
    newFile(name, text)


def urlDownload(url, index):
    data = requests.get(url)
    content = data.content
    # typeName = imghdr.what(None, content)


#
def baseDownload(coding, index):
    bs64_str = coding.replace('data:image/gif;base64,', '')
    bs64_str = base64.b64decode(bs64_str)
    # typeName = imghdr.what(None, bs64_str)


# # 打开文件，重新写入，或直接新建文件
def newFile(name, content):
    contentHtml = open(name + '.html', 'w', encoding='utf-8')
    contentHtml.write(content)
    contentHtml.close()
