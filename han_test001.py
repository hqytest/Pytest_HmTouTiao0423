# 导包
import logging


#新建类
class MyLogger:

    #新建一个日志器变量
    logger = None

    #新建获取日志器的方法
    @classmethod
    #判断日志器为空：
    def get_logger(cls):
        #获取日志器
        if cls.logger is None:
             #修改默认级别
            logging.basicConfig(level=logging.INFO)
            #获取处理器
            handler = logging.StreamHandler()
            #获取格式器
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            #将格式器添加到处理器中
            handler.setFormatter(formatter)
            #将处理器添加到日志器中
            cls.logger.addHandler(handler)
        #返回日志器
        return cls.logger
