# -*- coding: utf-8 -*-
import socket

host = '127.0.0.1'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
line = raw_input(" > ")
s.sendall(line + "\n")
