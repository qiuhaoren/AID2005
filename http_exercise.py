from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
while True:
    c,addr = s.accept()
    print("Connect from:",c) # 浏览器连接
    data = c.recv(4096) # 接收的是http请求
    print(data.decode().split('\r\n')[0]) # 请求行

    f = open('index.html','r')

    info = f.read()

    html = """HTTP/1.1 200 OK
    Content-Type:text/html
    
    %s
    """%info

    c.send(html.encode())
    f.close()
    c.close()

s.close()