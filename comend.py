#_author_ = 'wrx'
from socket import *
import time
import threading
import binascii

allClose = b"\x01\x0F\x00\x00\x00\x08\x01\x00\xFE\x95"
cllOpen = b"\x01\x0F\x00\x00\x00\x08\x01\xFF\xBE\xD5"
search = b"\x01\x01\x00\x00\x00\x08\x3D\xCC"
oneOpen = b"\x01\x05\x00\x00\xFF\x00\x8C\x3A"
oneClose = b"\x01\x05\x00\x00\x00\x00\xCD\xCA"
twoOpen = b"\x01\x05\x00\x01\xFF\x00\xDD\xFA"
twoClose = b"\x01\x05\x00\x01\x00\x00\x9C\x0A"

oneCtwoO = ['0x1', '0x1', '0x1', '0x2', '0xd0', '0x49']
oneOtwoC = ['0x1', '0x1', '0x1', '0x1', '0x90', '0x48']
allC = ['0x1', '0x1', '0x1', '0x0', '0x51', '0x88']
allO = ['0x1', '0x1', '0x1', '0x3', '0x11', '0x89']

# if __name__ == "__main__":
HOST = '192.168.1.68'
PORT = 8222
BUFSIZE = 1024
ADDR = (HOST,PORT)

lock = threading.Lock()

def commend(open):
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR)
        tcpCliSock.settimeout(5)
        print('连接成功')
        tcpCliSock.send(open)
        data = tcpCliSock.recv(BUFSIZE)
        dataStr = str(binascii.b2a_hex(data))[2:-1]
        dataList = [hex(x) for x in bytes(data)]
        print(dataStr)
    except Exception as e:
        print(e)
        tcpCliSock.close()

def searchs(s):
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR)
        tcpCliSock.settimeout(5)
        print('连接成功')
        while True:
            inp = input('请输入>>>>')
            if inp != '0':
                tcpCliSock.send(search)
                data = tcpCliSock.recv(BUFSIZE)
                dataStr = str(binascii.b2a_hex(data))[2:-1]
                dataList = [hex(x) for x in bytes(data)]
                print(dataStr)
                time.sleep(s)
            else:
                break
    except Exception as e:
        print(e)
        tcpCliSock.close()

def test(s):
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    try:
        tcpCliSock.connect(ADDR)
        tcpCliSock.settimeout(5)
        print('连接成功')
        while True:
            inp = input('请输入>>>>')
            if inp == '绿色':
                tcpCliSock.send(twoClose)
                data = tcpCliSock.recv(BUFSIZE)
                dataStr = str(binascii.b2a_hex(data))[2:-1]
                dataList = [hex(x) for x in bytes(data)]
                print(dataStr)
                # time.sleep(s)
            elif inp == '红色':
                tcpCliSock.send(twoOpen)
                data = tcpCliSock.recv(BUFSIZE)
                dataStr = str(binascii.b2a_hex(data))[2:-1]
                dataList = [hex(x) for x in bytes(data)]
                print(dataStr)
            elif inp == '啥颜色？':
                tcpCliSock.send(search)
                data = tcpCliSock.recv(BUFSIZE)
                dataStr = str(binascii.b2a_hex(data))[2:-1]
                dataList = [hex(x) for x in bytes(data)]
                if dataStr[6:8] == '00':
                    print('绿色亮着呢')
                else:
                    print('红色亮着呢')
            else:
                break
    except Exception as e:
        print(e)
        tcpCliSock.close()