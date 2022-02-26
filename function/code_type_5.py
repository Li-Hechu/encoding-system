"""生成防伪码"""
import os
import random

path = os.path.dirname(__file__)
path = os.path.dirname(path)
path1 = os.path.join(path, "data_analyse.ini")
path2 = os.path.join(path, "code\code4.txt")


def scode5():
    """根据配置文件批量添加带数据分析功能的防伪码"""
    global path1, path2
    file = open(path1, "r")
    f = open(path2, "a+")
    info_list = file.read()
    info_list = info_list.split("\n")
    for item in info_list:
        data = item.split(",")[0]
        count = item.split(",")[1]
        for i in range(int(count)):
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
    file.close()
    print("数据分析防伪码生成完成。文件保存在：", path2)
