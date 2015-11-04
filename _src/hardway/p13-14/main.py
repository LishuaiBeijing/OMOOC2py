# -*- coding: utf-8 -*-

####################
##练习argv
####################
from sys import argv

script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

####################
## 设置raw_input的提示符
####################
prompt = "> "
print "Where do you live?"
likes = raw_input(prompt)
print """
You live in %r
""" %likes
