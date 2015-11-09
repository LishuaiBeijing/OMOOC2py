# -*- coding: utf-8 -*-

####################
## 函数参数的特殊用法
####################
'''
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
print_two("Zed","Shaw")
'''
####################
## 按行读文件
####################

from sys import argv
script, input_file = argv
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)
print "First, let's print the whole file:\n"
print_all(current_file)

print "Let's rewind."
rewind(current_file)  # seek(0)用来将文件指针重新定位到文件头，这样才能从头开始打印

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) # 这里的三次打印说明，文件读的过程中，指针是全局变量，这大约涉及到python命名空间的知识

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
