import requests
from bs4 import BeautifulSoup

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
    content = getContent.getText(refiningData)
    content = content.json()
    htmlContent = BeautifulSoup(content['content'], 'html.parser')
    # contentRefining(htmlContent)
    htmlContent = htmlContent.prettify()
    newFile(content['tl'], htmlContent)


# def contentRefining(htmlContent):
#     paraData = htmlContent.find_all('para')
#     for i in paraData:
#         if(i.contents[1].string):
#             print(i.contents[1].string)


# # 打开文件，重新写入，或直接新建文件
def newFile(name, content):
    contentHtml = open(name + '.html', 'w', encoding='utf-8')
    contentHtml.write(content)
    contentHtml.close()
