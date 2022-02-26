"""添加防伪码"""
import os
import random
import sys
sys.path.append("../")
from 企业编码生成系统.input import winput

os.chdir(os.path.dirname(__file__))


def add_code1():
    """添加六位防伪码"""
    f = open("../code/code1.txt", "a+")
    card = f.readlines()  # 返回值为列表形式
    card = set(card)
    len1 = len(card)
    count = winput(1)
    for i in range(int(count)):
        randinfo = ""
        for j in range(6):
            randinfo += random.choice("123456789")
        randinfo += "\n"
        if randinfo not in card:
            f.write(randinfo)
            card.add(randinfo)
    f.close()
    len2 = len(card)
    print("防伪码添加完成，新添加防伪码", len2 - len1, "个,文件保存在：", os.path.realpath("../code/code1.txt"))


def add_code2():
    """添加商品系列防伪码"""
    f = open("../code/code2.txt", "a+")
    three = []  # 前三位
    six = []  # 后六位
    j = -1
    card = f.readlines()
    for i in range(len(card)):
        if card[i][:3] not in three:
            three.append(card[i][:3])
            six.append([])
            j += 1
        if card[i][3:] not in six:
            six[j].append(card[i][3:])
    info = winput(2)
    for i in range(info[1]):
        for j in range(info[2][i]):
            randinfo = str(int(info[0]) + i)
            for k in range(6):
                randinfo += random.choice("123456789")
            randinfo += "\n"
            if randinfo[:3] in three:
                if randinfo[3:] not in six:
                    f.write(randinfo)
                else:
                    pass
            else:
                f.write(randinfo)
    len2 = len(f.readlines())
    print("防伪码添加完成，新添加防伪码", len2 - len(card), "个，文件保存在：", os.path.abspath("../code/code2.txt"))


def add_code3():
    """添加25位商品序列号"""
    j = 0
    letter = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    count = winput(3)
    f = open("../code/code3.txt", "a+")
    code = f.readlines()  # 存储已有防伪码
    for i in range(count):
        randinfo = ""
        for j in range(25):
            randinfo += random.choice(letter)
        rand_info = randinfo[:5] + "-" + randinfo[5:10] + "-" + randinfo[10:15] + "-" + randinfo[15:20] \
                    + "-" + randinfo[20:25] + "\n"
        if rand_info not in code:
            f.write(rand_info)
            j += 1
    f.close()
    print("25位产品序列码添加完成，一共添加", j, "个，文件保存在：", os.path.abspath("../code/code3.txt"))


def add_code4():
    """添加带分析功能的防伪码"""
    total = 0
    f = open("../code/code4.txt", "a+")
    code = f.readlines()
    data = []
    number = []
    j = -1
    for i in range(len(code)):
        remove_digits = code[i].maketrans("", "", "1234567890")
        res_letter = code[i].translate(remove_digits)
        nres_letter = list(res_letter)
        info = nres_letter[0] + nres_letter[1] + nres_letter[2]
        if info not in data:
            data.append(info)
            number.append([])
            j += 1
        code[i].replace(data[j][0], "")
        code[i].replace(data[j][1], "")
        code[i].replace(data[j][2], "")
        number[j].append(code[i])
    meta = winput(4)
    for i in range(meta[0]):
        fir = meta[1][0].upper()
        sec = meta[1][1].upper()
        thi = meta[1][2].upper()
        randinfo = random.sample("123456789", 3)
        randinfo = sorted(randinfo)
        letterone = ""
        for j in range(9):
            letterone += random.choice("123456789")
        _info = str(letterone[0:int(randinfo[0])]) + fir + str(letterone[int(randinfo[0]):int(randinfo[1])]) \
               + sec + str(letterone[int(randinfo[1]):int(randinfo[2])]) + thi + str(
            letterone[int(randinfo[2]):9]) + "\n"
        if fir+sec+thi in data:
            if letterone not in number[data.index(fir+sec+thi)]:
                f.write(_info)
                total += 1
        else:
            f.write(_info)
            total += 1
    print("数据分析功能的防伪码生成完成，一共生成",total,"个，文件保存在：",os.path.abspath("../code/code4.txt"))
