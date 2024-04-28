import sys
import os

#在__init__.py中的以下代码在scripts目录下的py文件执行前都会默认调用
# sys.path是一个列表，它定义了Python解释器在查找模块时应该搜索的目录序列
# 添加当前工作目录到Python的模块搜索路径中，防止导包时找不到包的问题出现
sys.path.append(os.getcwd())
# print(os.getcwd())
# print(sys.path)