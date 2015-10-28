# -*- coding: utf-8 -*-
# python tutorial

import os

def main():
    print "Hello World!"
    print "这是 Bob\'的问候"

    foo(5,10)

    print '*' * 10
    print "this will execute " + os.getcwd()
   
    counter = 0
    counter += 1

    food = {'apple','xingzi','lizi','li'}
    for i in food:
        print i

def foo(pa,secondpa):
    res = pa+secondpa
    print '%s plus %s is %s'%(pa,secondpa,res)
    if res<50:
        print "zhege"
    elif (res>=50) and ((pa==42) or (secondpa==24)):
        print "nage"
    else:
        print "En..."
    return res  
    '''multi-line 
comments '''

if __name__=='__main__':
    main()
    
    
    




