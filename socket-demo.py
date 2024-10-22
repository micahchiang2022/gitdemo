import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverName = '47.101.161.112'
port = 10000

try:
    s.connect((serverName, port))
    s.send(b'hello')
    print(s.recv(1024))
except Exception as e:
    print(e)