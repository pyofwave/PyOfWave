import socket

HOST = "localhost"
PORT = 9283

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("#aname")
s.send("[tests.operation")
s.send("foo : bar")
s.close()