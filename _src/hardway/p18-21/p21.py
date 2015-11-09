# -*- coding: utf-8 -*-

###################
## 函数的嵌套
###################
def add(a, b):
    print "Adding %d + %d" % (a, b)
    dd = 9
    return a + b	

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b
	
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = 50
what = add(age, subtract(height, multiply(weight, iq)))
print what
