# -*- coding: utf-8 -*-
##################################
# 未完成：记录常用转义词
##################################

## 打印技巧
x = "There are %d types of people." % 10
y = 5.0
print "I said: %r." % x  # %r代替的不是打印输出结果，而是原始数据raw data
print "I said: %r" % y

print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
print end1 + end2 + end3, # 打印时用空格，会多一个空格，但是打印在一行里
print end4 + end5 + end6
print end1 + end2 + end3  # 去掉逗号，对比打印结果
print end4 + end5 + end6

months = "Jan\nFeb\nMar\n"
print "Months are %r." % months
print "Months are %s." % months

persian_cat = "I'm \\ a \\ cat." # 以\开头的转义词有很多，需要记录在笔记里
fat_cat = """
\t* cat food
\t* fishes
"""
print persian_cat
print fat_cat

## 获取屏幕输入
print "How old are you?", 
age = raw_input()
print "So you are %d years old." % int(age) # raw_input的输入默认为string类型

age = raw_input("How old are you?") #与上文用法相同
print "So you are %d years old." % int(age) 




