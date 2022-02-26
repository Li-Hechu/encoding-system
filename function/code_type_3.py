"""生成防伪码"""
import os
import random

path = os.path.dirname(__file__)
path = os.path.dirname(path)
path = os.path.join(path,"code\code3.txt")

letter = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"


def scode3(count:int):
    """生成25位产品序列码"""
    f = open(path, "a+")
    for i in range(count):
        randinfo = ""
        for j in range(25):
            randinfo += random.choice(letter)
        rand_info = randinfo[:5] + "-" + randinfo[5:10] + "-" + randinfo[10:15] + "-" + randinfo[15:20] \
                    + "-" + randinfo[20:25] + "\n"
        f.write(rand_info)
    f.close()
    print("25位序列生成完成，文件保存在：", path)
