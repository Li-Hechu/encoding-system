"""本模块用于介绍改系统"""


def introduction():
    """介绍该程序"""
    print(  # 有36个“=”
        """
        ====================================
            欢迎使用企业编码系统1.0(控制台版)
        ====================================
                        说明
        1.本程序的设计人员为LHC，未经允许，不可以
        转载、传播和复制。
        2.本程序主要用于企业生成编码。
        3.本系统的功能有：生成6位防伪码，生成9位系列
        产品码，生成25位产品序列码，生成12位带数据
        分析功能的编码，生成条形码和二维码。更多的
        功能正在开放中，敬请期待。
        4.根据各个功能前面的序号选择功能。
        ====================================
        """,
        end=" ")
    print(
        """
        1.生成6位防伪码
        2.生成9位系列产品码
        3.生成25位产品序列码
        4.生成12位带数据分析功能的编码
        5.根据配置文件批量生成12位带数据分析功能
          的编码
        6.生成条形码
        7.生成二维码
        8.向已有编码中添加新的编码，主要为1，2，3，
          4中码
        ====================================
        """,
        end=" ")
    print("按下<Enter>键以开始。")
    input("        ====================================")