from socket import * 
from threading import Thread 
import sys

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def client_handle(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b"Receive your message")
    c.close()

#创建套接字
s = socket() 
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen()

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue 

    #创建线程,绑定函数执行具体客户端请求
    t = Thread(target = client_handle,args = (c,))
    t.setDaemon(True)
    t.start()







