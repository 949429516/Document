from socketserver import * 

#多进程 udp并发
class Server(ForkingMixIn,UDPServer):
    pass 

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            #接收消息
            data = self.rfile.readline().decode()
            if not data:
                break
            print(data)
            #发送消息
            self.wfile.write\
            (b"Receive your message")

server = Server(('127.0.0.1',8888),Handler)
server.serve_forever()