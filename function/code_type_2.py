"""生成防伪码"""
import os
import random
"""
这里有一个小坑，在main文件里面调用该文件时，是以main文件所在的路径为准，
而不是该文件，所以如果直接写成“../code/code2.txt”，会发生找不到文件的错误
正确的做法是使用绝对路径
"""
path = os.path.dirname(__file__)    #获取该文件所处文件夹名称，是绝对路径
path = os.path.dirname(path)    #获取该文件夹的上一级目录的绝对路径
path = os.path.join(path,"code\code2.txt")  #路径拼接

def scode2(start: str, s_count: int, count: list):
    """生成9位系列产品数字防伪码"""
    global path
    f = open(path, "a+")
    for i in range(s_count):
        for j in range(count[i]):
            randinfo = str(int(start) + i)
            for k in range(6):
                randinfo += random.choice("123456789")
            randinfo += "\n"
            f.write(randinfo)
    f.close()
    print("9位防伪编码生成完成，文件保存在：", path)
