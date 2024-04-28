"""
定义全局变量
"""
from tools.read_yaml import read_yaml


#1、请求URL
host = "http://api-toutiao-web.itheima.net"
#2、请求头
headers = {"Content-Type": "application/json"}
#3、文章id
article_id = None

#4、获取文章参数化数据
article_data = read_yaml("articles.yaml")
# print(article_data)

#将文章相关数据在初始化文件中定义，变量后续其他文件中都可以使用
#5、文章title
title = article_data[0][0]
#6、文章内容
content = article_data[0][1]
#7、文章频道id
channel_id = article_data[0][2]
#8、文章频道
channel = article_data[0][3]
