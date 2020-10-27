import requests

cookies = {
    'OUTFOX_SEARCH_USER_ID': '1838737018@10.169.0.84',
    'OUTFOX_SEARCH_USER_ID_NCOO': '1284171018.57845',
    '_ntes_nnid': 'e617771dbfa83c1ee7aad93cc12a8ae7,1603076434056',
    '_ga': 'GA1.2.1179951248.1603268401',
    '__yadk_uid': 'oFNI1RLp4gV9vJw21xodX4zmtbubOtM2',
    'Hm_lvt_30b679eb2c90c60ff8679ce4ca562fcc': '1603269033',
    '_gid': 'GA1.2.222812349.1603764672',
    'JSESSIONID': 'aaaQnW1xlFrnu4qtPKqvx',
    '_gat': '1',
    'Hm_lvt_daa6306fe91b10d0ed6b39c4b0a407cd':
    '1603271765,1603425146,1603764672,1603778116',
    'Hm_lpvt_daa6306fe91b10d0ed6b39c4b0a407cd': '1603778119',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer':
    'https://note.youdao.com/ynoteshare1/index.html?id=62218d1d8f42aea18e84d345e0e6923d&type=notebook',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = {
    "editorType": '1',
    "unloginId": '7bf14339-5843-ffe1-7965-21e3ea1487ae',
    "editorVersion": 'new-json-editor',
}


def getText(dataList):
    content = ''
    for i in range(len(dataList)):
        if (i == 0):
            content = requests.get(dataList[i]['url'],
                                   headers=headers,
                                   params=params,
                                   cookies=cookies)
    return content