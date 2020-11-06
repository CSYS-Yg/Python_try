import requests
cookies = {
    'XIAOEID': 'ba25be8f4fb4df3a706aeb089bbece33',
    'channel': 'homepage',
    'cookie_channel': 'homepage',
    'cookie_session_id': 'ZdH6WYoK8H8V4IvsMWw6iBWGuypD2JvW',
    'anonymous_user_key': 'dV9hbm9ueW1vdXNfNWZhMzVhN2E2MjNjYl9QRFhKRWQ3ZmNu',
    'dataUpJssdkCookie': '{"wxver":"","net":"","sid":""}',
    'sajssdk_2015_new_user_appt2ioq9ws3997_pc_xiaoe-tech_com': '1',
    'sensorsdata2015jssdkcross':
    '%7B%22%24device_id%22%3A%2217596197340e7-0cd2f6bad16205-625b7720-2073600-17596197341a4f%22%7D',
    'sa_jssdk_2015_appt2ioq9ws3997_pc_xiaoe-tech_com':
    '%7B%22distinct_id%22%3A%2217596197340e7-0cd2f6bad16205-625b7720-2073600-17596197341a4f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D',
    'pc_user_key': '71e4e17e10b45c7c0f328cd4c775e547',
    'userInfo':
    '{"app_id":"appt2iOQ9ws3997","user_id":"u_5e97a9f29a622_4NT5SONQ5U","wx_avatar":"http://wechatavator-1252524126.file.myqcloud.com/appt2iOQ9ws3997/image/compress/u_5e97a9f29a622_4NT5SONQ5U.png","wx_gender":1,"birth":null,"address":null,"job":null,"company":null,"wx_account":"","universal_union_id":"oTHW5v3NHLuqR1PwkW2DBseukSB0","can_modify_phone":1,"phone":"13243770866","pc_user_key":"71e4e17e10b45c7c0f328cd4c775e547","permission_visit":0,"permission_comment":0,"permission_buy":0}',
    'app_id': '"appt2iOQ9ws3997"',
    'superVipData': '{"hasSuperVip":false,"url":"","is_svip":0}',
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
    'Host':
    'appt2ioq9ws3997.pc.xiaoe-tech.com',
    'Origin':
    'https://appt2ioq9ws3997.pc.xiaoe-tech.com',
    'Referer':
    'https://appt2ioq9ws3997.pc.xiaoe-tech.com/detail/p_5e8d5ac3ada72_THibR5Zs/6',
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
    'goods_id': "p_5e8d5ac3ada72_THibR5Zs",
    'goods_type': 6,
    'last_id': "",
    'page_size': 20,
    'resource_type': [1, 2, 3, 4, 20]
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