import socket

HOST = "localhost"
PORT = 9283

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("#name1")
s.send("[tests.result")
s.send("foo:bar")
s.send("bar:foo")

while raw_input("press key and return to read:"):
    print s.recv(1024)
    
print "Error tests."
s.send("#aname2")
s.send("[tests.nonexistant")
s.send("#name3")
s.send("[tests.error")

while raw_input("press key and return to read:"):
    print s.recv(1024)

