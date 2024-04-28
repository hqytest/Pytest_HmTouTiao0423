
#导包,需要先安装包：pip install pyyaml
import yaml

from config import Base_Path


#定义函数
def read_yaml(filename):
    #文件路径定义：通过config.py中的项目基础路径Base_Path动态定义路径
    # 使用 pathlib 库的 Path 类时，你可以使用正斜杠 / 作为路径分隔符，无论你的代码是在任意类型的操作系统。
    # pathlib 会自动处理路径分隔符的转换，以适应底层操作系统的要求。
    filepath = Base_Path/"data"/filename

    #定义空列表，组装测试数据
    arr = []
    #遍历，调研yaml.safe.load(f).values()方法
    with open(filepath, "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f).values()
        for data in datas:
            arr.append(tuple(data.values()))

    #返回结果
    return arr


if __name__ == '__main__':
    print(read_yaml("login.yaml"))
