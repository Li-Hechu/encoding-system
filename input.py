"""本模块用与控制输入"""


def winput(number: int):
    """通过数字选择不同编码的输入方式"""
    if number == 1:
        count = input("请输入需要生成的6位防伪码的数量：")
        while int(count) <= 0:
            count = input("您的输入不合法，请重新输入：")
        return int(count)
    elif number == 2:
        count = []
        start = input("请输入产品数字起始号(3位)：")
        while len(start) != 3:
            start = input("您输入的起始号不为三位，请重新输入：")
        scount = input("请输入产品的系列数量：")
        while int(scount) <= 0:
            scount = input("数量应该大于0，请重新输入：")
        for i in range(int(scount)):
            temp = int(input("请输入第%d个系列产品的数量：" % (i + 1)))
            count.append(temp)
        return start, int(scount), count
    elif number == 3:
        count = input("请输入需要生成的25位防伪码的数量：")
        while int(count) <= 0:
            count = input("数量应该大于0，请重复输入：")
        return int(count)
    elif number == 4:
        count = input("请输入要生成的带数据分析功能的防伪码数量：")
        while int(count) <= 0:
            count = input("数量应该大于0，请重新输入：")
        data = input("请输入三位数据分析编号：")
        while len(data) != 3:
            data = input("输入的编号不为3位，请重新输入：")
        return int(count), data
    elif number == 6:
        code = []  # 保存商品编码
        nation = input("请输入三位国家代码：")  # 国家编码
        while len(nation) != 3 or int(nation) <= 0:
            nation = input("输入有误，请重新输入：")
        enterprise = input("请输入四位企业代码：")  # 企业编码
        while len(enterprise) != 4 or int(enterprise) <= 0:
            enterprise = input("输入有误，请重新输入：")
        print("请输入五位商品代码(键入0结束输入)")
        while True:
            goods = input()  # 商品编码
            if goods != "0":
                while len(goods) != 5 or int(goods) <= 0:
                    goods = input("输入有误，请重新输入：")
                code.append(goods)
            else:
                print("输入完成。")
                break
        return code,nation,enterprise
    elif number == 7:
        code = ""
        qr_code = []
        print("请批量输入二维码的编码(输入0结束)：")
        while code != "0":
            code = input()
            qr_code.append(code)
        return qr_code