import requests

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
    print(refiningData)
