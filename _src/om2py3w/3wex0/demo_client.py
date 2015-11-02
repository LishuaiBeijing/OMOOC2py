# -*- coding: utf-8 -*-
import socket

host = '127.0.0.1'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall('Hello World')
data = s.recv(1024)
s.close()
print 'Received',repr(data)
