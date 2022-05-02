import json
import requests
from socket import *

from pprint import pprint

class bot:
    def __init__(self) -> None:
        pass
        
    def message(data):
        url='http://api.qingyunke.com/api.php?key=free&appid=0&msg={data}'.format(data=data.decode())
        sess = requests.get(url)
        answer = sess.text
        answer = json.loads(answer)["content"]
        print(answer)
        return answer

        
    def client_handler():
        HOST = '127.0.0.1'
        PORT = 9000
        BUFSIZ = 1024
        ADDRESS = (HOST, PORT)

        tcpServerSocket = socket(AF_INET, SOCK_STREAM)
        tcpServerSocket.bind(ADDRESS)
        print("服务器启动，监听端口{}...".format(ADDRESS[1]))
        tcpServerSocket.listen(5)

        try:
            while True:
                print('服务器正在运行，等待客户端连接...')

                client_socket, client_address = tcpServerSocket.accept()
                print('客户端{}已连接！'.format(client_address))

                try:
                    while True:

                        data = client_socket.recv(2048)
                        if data:
                            print('接收到消息 {}({} bytes) 来自 {}'.format(data.decode('utf-8'), len(data), client_address))
                            # 返回响应数据，将客户端发送来的数据原样返回
                            client_socket.send(bot.message(data).encode())
                            print('响应消息 {} 至 {}'.format(data.decode(), client_address))
                        else:
                            print('客户端 {} 已断开！'.format(client_address))
                            break
                finally:
                    client_socket.close()
        finally:
            tcpServerSocket.close()
bot.client_handler()





        