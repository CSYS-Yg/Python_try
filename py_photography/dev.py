import logging
import requests

import parameter

# 定义日志相关内容
logging.basicConfig(
    format='' +
    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)
handler = logging.FileHandler(filename='geek_crawler.log',
                              mode='w',
                              encoding='utf-8')
log = logging.getLogger(__name__)
log.addHandler(handler)


class RequestError(Exception):
    """ 请求错误 """
    pass


class NotValueError(Exception):
    """ 没有内容错误 """
    pass


class Cookie:
    # 默认方法，初始化 Cookie 类时，会自动执行
    # self 为默认 类 的实例。指向他的本身
    def __init__(self, cookie_string=None):
        self._cookies = {}
        if cookie_string:
            self.load_string_cookie(cookie_string)

    def load_string_cookie(self, cookie_str):
        """
        从字符串中加载 Cookie 的方法（将字符串转换成字典形式）, 相当于 cookie_string 方法的逆反操作
        Args:
            cookie_str: 字符串形式的 Cookies，一般是从抓包请求中复制过来
                eg: gksskpitn=cc662cd7-0a39-430a-a603-a1c61d6f784f; LF_ID=1587783958277-6056470-8195597;
        Returns:
        """
        cookie_list = cookie_str.split(';')
        res = self.list_to_dict(cookie_list)
        self._cookies = {**self._cookies, **res}

    def list_to_dict(lis):
        """
        列表转换成字典的方法
        Args:
            lis: 列表内容
        Returns:
            转换后的字典
        """
        result = {}
        for ind in lis:
            try:
                ind = ind.split('=')
                result[ind[0]] = ind[1]
            except IndexError:
                continue
        return result


# 创建一个极客时间操作类
class GeekCrawler:
    def __init__(self, cellphone=None, passwd=None):
        self.cellphone = cellphone
        self.password = passwd
        self.cookie = Cookie(
            "LF_ID=1587783958277-6056470-8195597;_ga=GA1.2.880710184.1587783959;"
            "_gid=GA1.2.1020649675.1587783959; SERVERID=1fa1f330efedec1559b3abbc"
            "b6e30f50|1587784166|1587783958; _gat=1;Hm_lvt_022f847c4e3acd44d4a24"
            "81d9187f1e6=1587775851,1587775917,1587783916,1587784202; Hm_lpvt_02"
            "2f847c4e3acd44d4a2481d9187f1e6=1587784202;")
        self.common_headers = {
            "Accept":
            "application/json, text/plain, */*",
            "Accept-Encoding":
            "gzip, deflate, br",
            "Accept-Language":
            "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control":
            "no-cache",
            "Connection":
            "keep-alive",
            "Pragma":
            "no-cache",
            "Sec-Fetch-Dest":
            "empty",
            "Sec-Fetch-Mode":
            "cors",
            "Sec-Fetch-Site":
            "same-origin",
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/81.0.4044.122 Safari/537.36"
        }
        self.products = []

    def _login(self):
        """ 登录接口方法 """
        log.info("请求登录接口：")
        url = "https://account.geekbang.org/account/ticket/login"
        method = "POST"
        headers = deepcopy(self.common_headers)
        headers["Host"] = "account.geekbang.org"
        headers["Origin"] = "https://account.geekbang.org"
        headers["Cookie"] = self.cookie.cookie_string
        params = {
            "country": 86,
            "cellphone": self.cellphone,
            "password": self.password,
            "captcha": "",
            "remember": 1,
            "platform": 3,
            "appid": 1,
            "source": ""
        }

        log.info(f"接口请求参数：{params}")
        res = requests.request(method, url, headers=headers, json=params)

        if (res.status_code != 200) or (str(res.json().get('code', ''))
                                        == '-1'):
            log.info(f"此时 products 的数据为：{self.products}")
            log.error(f"登录接口请求出错，返回内容为：{res.content.decode()}")
            raise RequestError(f"登录接口请求出错，返回内容为：{res.content.decode()}")
        self.cookie.load_set_cookie(res.headers['Set-Cookie'])
        log.info('-' * 40)


# 整体操作流程
def requestOrder(cellphone, passwd):
    # 初始化模拟 GeekCrawler 类请求数据
    geek = GeekCrawler(cellphone, passwd)


if __name__ == '__main__':
    try:
        requestOrder(parameter.cellphone, parameter.pwd)
    except Exception:
        import traceback
        log.error(f"请求过程中出错了，出错信息为：{traceback.format_exc()}")
    finally:
        print('try-finally 语句无论是否发生异常都将执行最后的代码。')
