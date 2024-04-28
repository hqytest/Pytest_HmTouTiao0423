from pathlib import Path

#使用 pathlib 库的 Path 类时，你可以使用正斜杠 / 作为路径分隔符，无论你的代码是在任意类型的操作系统。
# pathlib 会自动处理路径分隔符的转换，以适应底层操作系统的要求。

# 1、定义基础路径,不能使用Path.cwd()
# Path.cwd():获取当前工作目录,
# 其他目录路径下的B代码文件调用它执行时，工作目录就变为B代码文件的目录了
# Base_Path = Path(Path.cwd())

#2、 定义基础路径
#__file__是Python中的一个内置变量，它表示当前文件的文件名
# Path(__file__)获取当前测试脚本的目录路径，不会在被其他路径下的代码调用时发生变化
# Path(__file__).parent：获取当前测试脚本的目录名
Base_Path = Path(__file__).parent
print(Base_Path)
