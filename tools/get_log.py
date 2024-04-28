#导包
import logging.handlers
import time

from config import Base_Path


#新建类
class GetLog:
    #新建一个日志器变量
    __logger = None

    #新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        #判断日志器为空：
        if cls.__logger is None:
            # 获取日志器：日志器是logging库的核心，负责记录和处理日志消息。
            cls.__logger = logging.getLogger()

            #日志级别如下，从高到低：
            #1、CRITICAL：严重错误，会导致应用程序退出
            #2、ERROR：错误，需要处理但不会导致应用程序退出
            #3、WARNING：警告，需要引起注意但不会导致应用程序退出
            #4、INFO：一般信息，默认级别
            #5、DEBUG：调试信息，用于开发和调试阶段
            # 修改默认日志级别
            cls.__logger.setLevel(logging.INFO)
            log_path = Base_Path/"log"/"hmtt_{}.log".format(time.strftime("%y-%m-%d"))

            #获取处理器:每天午夜滚动日志，并且保留最近的三个日志文件
            # TimedRotatingFileHandler:一个处理器，可以根据时间间隔（如每天、每周等）来自动滚动（即创建新的）日志文件
            # 参数说明：
            # filename是日志文件的路径，
            # when指定了滚动的时间间隔（如'midnight'表示每天午夜），
            # interval是滚动的时间间隔单位（如1表示每天），
            # backupCount是保留的旧日志文件的数量
            handler = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            #获取格式器:包括了时间戳、日志级别、文件名、函数名、行号和日志消息。
            fmt = "%(asctime)s  %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)]- %(message)s"
            formatter = logging.Formatter(fmt)
            #将格式器添加到处理器中
            handler.setFormatter(formatter)
            #将处理器添加到日志器中
            cls.__logger.addHandler(handler)
        #返回日志器
        return cls.__logger


if __name__ == '__main__':
    #获取日志器实例
    log = GetLog.get_logger()
    log.info("测试信息级别日志")
    log.error("测试错误级别")
