"""
目标：定义类实现：
        1、提取token
        2、断言响应结果
"""
import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class Tool:
    #新建类方法：提取token
    @classmethod
    def common_token(cls, response):
        # 提取token
        token = response.json().get("data").get("token")
        # 追加请求头headers
        api.headers["Authorization"] = "Bearer " + token
        log.info(f"正在提取token，提取后的headers为:{api.headers}")
        # 打印追加token后的headers
        print("追加token后的headers为：", api.headers)

    #新建类方法：断言响应结果
    @classmethod
    #状态码status_code默认值设置为201
    def common_assert(cls, response, status_code=201):
        log.info(f"正在调用公共断言方法！")
        # 断言响应结果
        assert status_code == response.status_code
        assert "OK" == response.json().get("message")
