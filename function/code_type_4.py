"""生成防伪码"""
import os
import random

path = os.path.dirname(__file__)
path = os.path.dirname(path)
path = os.path.join(path, "code\code4.txt")


def scode4(count: int, data: str):
    """
    生成含数据分析功能的编码
    三位的分析编号分别表示地区，颜色和产品批次
    """
    global path
    scode4_5(count, data, path)
    print("数据分析防伪码生成完成。文件保存在：", path)


def scode4_5(count: int, data: str, _path):
    """添加带数据分析功能的防伪码的公用方法"""
    f = open(_path, "a+")
    for i in range(count):
        fir = data[0].upper()
        sec = data[1].upper()
        thi = data[2].upper()
        randinfo = random.sample("123456789", 3)
        randinfo = sorted(randinfo)
        letterone = ""
        for j in range(9):
            letterone += random.choice("123456789")
        info = str(letterone[0:int(randinfo[0])]) + fir + str(letterone[int(randinfo[0]):int(randinfo[1])]) \
               + sec + str(letterone[int(randinfo[1]):int(randinfo[2])]) + thi + str(
            letterone[int(randinfo[2]):9]) + "\n"
        f.write(info)
    f.close()
