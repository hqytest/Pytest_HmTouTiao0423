"""
目标：登录、发布文章接口API封装
"""
import random

#导包
import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()

#定义接口类
class ApiTouTiao:
    #初始化
    def __init__(self):
        #1、登录接口url
        self.url_login = api.host + "/mp/v1_0/authorizations"
        log.info(f"正在初始化登录url:{self.url_login}")
        # 2、发布文章接口url
        self.url_articles = api.host + "/mp/v1_0/articles?draft=false"
        log.info(f"正在初始化发布文章url:{self.url_articles}")

    #定义请求方法：登录接口
    def api_login_post(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        #定义请求体
        data = {"mobile": mobile, "code": code}
        log.info(f"正在调用登录接口，请求数据为:{data}")
        #调用登录的post请求并返回响应对象
        #注意：请求数据的接受参数为json，因为headers中的content-type为json
        return requests.post(url=self.url_login, headers=api.headers, json=data)

    #定义请求方法：发布文章接口
    def api_articles_post(self, title, content, channel_id):
        # 定义请求体
        data = {"title": title, "content": content, "imgType": "single",
                "channel_id": channel_id,
                "cover": {"type": 1, "images": ["http://toutiao-img.itheima.net/FlroLEiqEi1nKPzWennulkyx3-th"]}}

        log.info(f"正在调用发布文章接口，请求数据为:{data}")
        # 调用登录的post请求并返回响应对象
        #注意：请求数据的接受参数为json，因为headers中的content-type为json
        return requests.post(url=self.url_articles, headers=api.headers, json=data)
