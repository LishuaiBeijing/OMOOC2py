# -*- coding: utf-8 -*-
# 简单的网络式交互日记本 -- 服务端

from diary_func import *
import socket

host = ''
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()  # 监听指定端口的信息，收到信息则执行下面的代码

diary_file = open("diary",'a') #追加写入日记本
while 1:
    data = conn.recv(1024)
    if not data:break
    diary_file.write(data)
conn.close()
diary_file.close()

diary_file = open("diary",'r')
printdiary(diary_file) #打印出所有的日记
diary_file.close() 
