import requests
# from bs4 import BeautifulSoup
import json

cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '1910243514.2997293',
    'JSESSIONID': 'aaaSHHq7GTIvz-4FUWavx',
    'Hm_lvt_daa6306fe91b10d0ed6b39c4b0a407cd': '1603270200',
    'Hm_lpvt_daa6306fe91b10d0ed6b39c4b0a407cd': '1603270200',
    '_ga': 'GA1.2.1086818050.1603270200',
    '_gid': 'GA1.2.1798088565.1603270200',
    '_gat': '1',
    'OUTFOX_SEARCH_USER_ID': '^\\^2004762860^@10.169.0.83^\\^',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer':
    'https://note.youdao.com/ynoteshare1/index.html?id=62218d1d8f42aea18e84d345e0e6923d^&type=notebook',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = (
    ('editorType', '1^'),
    ('unloginId', 'daa1ea6a-87a5-e5a9-f14f-8f32b59d3f28^'),
    ('editorVersion', 'new-json-editor'),
)

response = requests.get(
    'https://note.youdao.com/yws/public/notebook/62218d1d8f42aea18e84d345e0e6923d/subdir/9D3030DCC7734AC3BBA0A01DAECF50B0',
    headers=headers,
    params=params,
    cookies=cookies)
jsonResponse = json.dumps(response.json(),
                          sort_keys=True,
                          indent=4,
                          separators=(',', ':'))

test = json.loads(jsonResponse)

test = json.dumps(test, sort_keys=True, indent=4, separators=(',', ':'))

print(test)

# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())