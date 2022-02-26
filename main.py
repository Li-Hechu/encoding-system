"""此模块为程序的入口"""
#!C:\Python\python.exe
from function.add_code import *
from function.code_type_1 import scode1
from function.code_type_2 import scode2
from function.code_type_3 import scode3
from function.code_type_4 import scode4
from function.code_type_5 import scode5
from function.code_type_6 import scode6
from function.code_type_7 import scode7
from input import winput
from introduction import introduction
import time

introduction()
while True:
    number = int(input("请输入功能序号(输入0结束程序)："))
    if number == 0:
        break
    elif number == 1:
        count = winput(1)
        scode1(count)
    elif number == 2:
        info = winput(2)
        scode2(info[0], info[1], info[2])
    elif number == 3:
        count = winput(3)
        scode3(count)
    elif number == 4:
        info = winput(4)
        scode4(info[0], info[1])
    elif number == 5:
        scode5()
    elif number == 6:
        info = winput(6)
        scode6(info[0], info[1], info[2])
    elif number == 7:
        qr_code = winput(7)
        scode7(qr_code)
    elif number == 8:
        num = int(input("请输入需要添加的防伪码序号："))
        check = [1, 2, 3, 4]
        while num not in check:
            num = int(input("无法添加您所输入的防伪码型号，请重新输入："))
        if num == 1:
            add_code1()
        elif num == 2:
            add_code2()
        elif num == 3:
            add_code3()
        elif num == 4:
            add_code4()
