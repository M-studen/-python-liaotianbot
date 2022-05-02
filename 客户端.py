from socket import *

HOST = '127.0.0.1'
PORT = 9000
BUFSIZ = 1024
ADDRESS = (HOST, PORT)

tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(ADDRESS)

while True:
    data = input('>>>')
    if not data:
        break

    # 发送数据
    tcpClientSocket.send(data.encode('utf-8'))
    # 接收数据
    data, ADDR = tcpClientSocket.recvfrom(BUFSIZ)
    if not data:
        break
    print("青云客：", data.decode('utf-8'))

print("链接已断开！")
tcpClientSocket.close()