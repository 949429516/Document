import gevent 
from gevent import monkey
#需要在socket导入前执行,改变socket的属性
monkey.patch_all()
from socket import * 

#套接字创建
def server(port):
    s = socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print('Connect from',addr)
        gevent.spawn(handle,c)

#处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print("recv:",data)
        c.send(b"Receive your message")
    c.close()

if __name__ == "__main__":
    server(8888)