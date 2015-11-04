# -*- coding: utf-8 -*-

####################
## 练习文件读写
####################
from sys import argv
from os.path import exists
script, filename = argv
txt = open(filename)
print "Here is your file %r" %filename
print txt.read()

txt.close()

####################
## 文件函数
####################
# 以w方式打开文件，会立即清空文件内容
# r+w 和 w+r 不同
# r+w不会清空文件内容，写入内容时也不会清空之前的内容，与a的区别在于可以先读后续写
# w+r会清空文件内容，因此与单独w没有区别
target = open(filename, 'r+w') #以w方式打开，会先清空文件内容
print "print the file:"
print target.read()

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print "print the file again:"
print target.read()

target.close()

in_file = open(filename)
indata = in_file.read()
print "The input file is %d bytes long." % len(indata) #len函数返回字节数
print "Does the file exist? %r" % exists(filename)
