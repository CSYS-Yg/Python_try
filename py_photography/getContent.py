import requests
cookies = {
    '_ga': 'GA1.2.1849169855.1595381186',
    'LF_ID': '1595381186235-8034655-9213653',
    'GCID': '0d35e97-1635b99-6ae4752-55e151e',
    'GRID': '0d35e97-1635b99-6ae4752-55e151e',
    '_gid': 'GA1.2.1000377831.1604398796',
    'GCESS':
    'BQYEjMy5JAQEAC8NAAoEAAAAAAEIyukaAAAAAAAHBN8OeE4CBNcuoV8MAQEDBNcuoV8FBAAAAAALAgUACQEBCAED',
    'sensorsdata2015jssdkcross':
    '%7B%22distinct_id%22%3A%221763786%22%2C%22first_id%22%3A%2217494b98c769ae-090f5634b41d5f-6854732c-2073600-17494b98c77bba%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Ftime.geekbang.org%2F%22%2C%22%24latest_utm_term%22%3A%22geektime-summary-100057601-bianjituijian%22%2C%22%24latest_utm_source%22%3A%22geektime%22%2C%22%24latest_utm_medium%22%3A%22summary%22%2C%22%24latest_utm_campaign%22%3A%22100057601%22%2C%22%24latest_utm_content%22%3A%22bianjituijian%22%7D%2C%22%24device_id%22%3A%221738dd8227b2c-080dd9dc7bb0cf-6b567921-2073600-1738dd8227cadd%22%7D',
    'gksskpitn': 'd1b30759-6d29-47ab-b2b1-359496068db3',
    'Hm_lvt_59c4ff31a9ee6263811b23eb921a5083':
    '1604453801,1604454261,1604455043,1604455388',
    'Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6':
    '1604453801,1604454261,1604455043,1604455389',
    'acw_tc': '2760777016044584202661009e95f337bd218ea6702894aad466228d00f793',
    'Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083': '1604458420',
    'Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6': '1604458420',
    '_gat': '1',
    'gk_process_ev':
    '{%22count%22:20%2C%22target%22:%22%22%2C%22referrer%22:%22https://time.geekbang.org/dashboard/course%22%2C%22referrerTarget%22:%22page_course_article_detail%22%2C%22utime%22:1604455930902}',
    'SERVERID': '3431a294a18c59fc8f5805662e2bd51e|1604460214|1604455388',
}

headers = {
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':
    'keep-alive',
    'Content-Type':
    'application/json',
    # 'Cookie':
    # '_ga=GA1.2.1849169855.1595381186; LF_ID=1595381186235-8034655-9213653; GCID=0d35e97-1635b99-6ae4752-55e151e; GRID=0d35e97-1635b99-6ae4752-55e151e; _gid=GA1.2.1000377831.1604398796; GCESS=BQYEjMy5JAQEAC8NAAoEAAAAAAEIyukaAAAAAAAHBN8OeE4CBNcuoV8MAQEDBNcuoV8FBAAAAAALAgUACQEBCAED; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221763786%22%2C%22first_id%22%3A%2217494b98c769ae-090f5634b41d5f-6854732c-2073600-17494b98c77bba%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Ftime.geekbang.org%2F%22%2C%22%24latest_utm_term%22%3A%22geektime-summary-100057601-bianjituijian%22%2C%22%24latest_utm_source%22%3A%22geektime%22%2C%22%24latest_utm_medium%22%3A%22summary%22%2C%22%24latest_utm_campaign%22%3A%22100057601%22%2C%22%24latest_utm_content%22%3A%22bianjituijian%22%7D%2C%22%24device_id%22%3A%221738dd8227b2c-080dd9dc7bb0cf-6b567921-2073600-1738dd8227cadd%22%7D; gksskpitn=d1b30759-6d29-47ab-b2b1-359496068db3; Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1604453801,1604454261,1604455043,1604455388; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1604453801,1604454261,1604455043,1604455389; acw_tc=2760777016044584202661009e95f337bd218ea6702894aad466228d00f793; _gat=1; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1604460212; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1604460212; gk_process_ev={%22count%22:20%2C%22target%22:%22%22%2C%22referrer%22:%22https://time.geekbang.org/dashboard/course%22%2C%22referrerTarget%22:%22page_course_article_detail%22%2C%22utime%22:1604455930902}; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1604460214|1604455388',
    'Host':
    'time.geekbang.org',
    'Origin':
    'https://time.geekbang.org',
    'Referer':
    'https://time.geekbang.org/column/intro/100043001',
    'Sec-Fetch-Dest':
    'empty',
    'Sec-Fetch-Mode':
    'cors',
    'Sec-Fetch-Site':
    'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.11 Safari/537.36'
}

params = {
    'cid': '100043001',
    'order': "earliest",
    'prev': 0,
    'sample': False,
    'size': 500,
}


# 请求接口，获取列表数据
def postData(url):
    data = requests.post(url,
                         headers=headers,
                         cookies=cookies,
                         params=params,
                         timeout=5)
    dataJson = data.json()
    print(dataJson)
    # refining(dataJson[2])