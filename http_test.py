from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

c,addr = s.accept()
print("Connect from:",c)
data = c.recv(4096)
print(data.decode())

html = """HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""
c.send(html.encode())

c.close()
s.close()