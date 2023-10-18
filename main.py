# coding=utf-8
import time

from dyGlobal import G_V

from dyUdp import dyUdp

def print_hi(name,msg):
    # 在下面的代码行中使用断点来调试脚本。
    print("Hi, {0},{1}".format(name,msg))  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm',"now我已运行程序！")
    # from dyRS485 import dyRS485

    udp = dyUdp(1, "udp", 1)
    udp.start()
    while True:
        udp.sendUdp("FE850053000000000000000A0101D60A010101FFFFFF0000000000434800000000EFFF011843484348EFFF013B4348000000004348010000271B0000000000000000000000000000000000000000000000000000000000ECAF")
        time.sleep(1)


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
