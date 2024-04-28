"""
目标：完成对登录、发布文章接口的业务层封装
"""
import allure
import pytest

import api
#导包
from api.api_TouTiao import ApiTouTiao
from tools.tool import Tool

from tools.get_log import GetLog

from tools.read_yaml import read_yaml

log = GetLog.get_logger()


# @allure.feature('Feature')
# @allure.story('Story')
#新建测试类
class TestTouTiao:
    #初始化
    def setup_class(self):
        #获取ApiTouTiao对象
        self.TouTiao = ApiTouTiao()

    # 新建测试方法：登录接口
    #pytest的参数化获取数据
    @pytest.mark.parametrize("mobile,code", read_yaml("login.yaml"))
    def test01_login(self, mobile, code):
        allure.description('This is an example test case.')
        #调用登录接口
        r = self.TouTiao.api_login_post(mobile, code)
        #打印响应内容
        print("登录接口的响应信息为：", r.json())
        try:
            #提取token的公共方法中有将token加到headers中，可供发布文章的请求中使用headers
            Tool.common_token(r)
            #断言响应状态码及响应信息：公共方法
            Tool.common_assert(r, 201)
        except Exception as e:
            #写日志,记录异常信息
            log.error("登录接口的异常信息为：{}".format(e))
            #抛异常
            raise e

        # #提取token和断言是公用的，可以在tool.py中实现
        # # 提取token
        # token = r.json().get("data").get("token")
        # #追加请求头headers
        # api.headers["Authorization"] = "Bear "+token
        # # 打印追加token后的headers
        # print("追加token后的headers为：", api.headers)
        # #断言响应结果
        # assert 201 == r.status_code
        # assert "OK" == r.json().get("message")

    #新建测试方法：发布文章接口
    # pytest的参数化获取数据
    @pytest.mark.parametrize("title,content,channel_id, channel", read_yaml("articles.yaml"))
    #测试方法的参数要与参数化获取参数一一对应
    def test02_articels(self, title, content, channel_id, channel):
        #调用发布文章接口
        r = self.TouTiao.api_articles_post(title, content, channel_id)
        #打印响应内容
        print("发布文章的信响应信息为：", r.json())
        #2、提取文章id
        api.article_id = r.json().get("data").get("id")
        log.info(f"正在提取文章id,文章id为：{api.article_id}")
        # print("发布文章成功后的id值为：", api.article_id)
        try:
            #3、断言
            Tool.common_assert(r)
        except Exception as e:
            log.error("发布文章接口的异常信息为：{}".format(e))
            raise


# if __name__ == '__main__':
#     pytest.main(['-s', 'test_toutiao.py'])
