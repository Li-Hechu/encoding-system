"""生成条形码"""
import os

from pystrich.ean13 import EAN13Encoder

path = os.path.dirname(__file__)
path = os.path.dirname(path)
path = os.path.join(path, "barcode")


def scode6(code: list, nation: str, enterprise: str):
    """生成条形码"""
    global path
    for i in range(len(code)):
        bar = nation + enterprise + code[i]
        check_num = (10 - (((int(bar[0]) + int(bar[2]) + int(bar[4]) + int(bar[6]) + int(bar[8])) * 3 + (
                    int(bar[1]) + int(bar[3])
                    + int(bar[5]) + int(bar[7]))) % 10)) % 10
        bar += str(check_num)
        encoder = EAN13Encoder(bar)
        os.chdir(os.path.realpath("../barcode"))
        encoder.save(bar + ".png")
    print("条形码输出完成，一共%d个，文件保存在：%s" % (len(code), path))
