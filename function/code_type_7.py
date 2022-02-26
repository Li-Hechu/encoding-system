"""二维码输出"""
import os

import qrcode

path = os.path.dirname(__file__)
path = os.path.dirname(path)
path = os.path.join(path, "qrcode")


def scode7(qr_code: list):
    """二维码的输出"""
    global path
    os.chdir(path)
    for i in range(len(qr_code) - 1):
        qr = qrcode.QRCode(version=2, box_size=10, border=4)
        qr.add_data(qr_code[i])
        qr.make(fit=True)
        img = qr.make_image()
        if qr_code[i][:8] == "https://":
            img.save(qr_code[i][8:] + ".png")
        else:
            img.save(qr_code[i] + ".png")
    print("二维码批量生成完成，共生成%d个二维码，文件位置在：%s" % (len(qr_code) - 1, path))
