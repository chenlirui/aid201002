"""
Author: Levi
Email: lvze@tedu.cn
Time : 2020-12-15
Env : Python3.6

socket and process exercise
"""
from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息的结构 {name:address}
user = {}

def do_login():
    pass


def do_chat():
    pass


def do_exit():
    pass


# 搭建总体逻辑结构
def main():
    # 创建udp套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    # 循环接收用户请求
    while True:
        data, addr = sock.recvfrom(1024)
        print(data.decode())
        # 根据请求，分情况讨论
        if data == "进入":
            do_login()
        elif data == "聊天":
            do_chat()
        elif data == "退出":
            do_exit()


if __name__ == '__main__':
    main()  # 启动