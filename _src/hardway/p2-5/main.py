# -*- coding:utf-8 -*-
# 这是一段注释
print "Hi # 这不是注释"
print "Rooters",25 + 30/5

# 数字计算，整数与浮点数，比较大小
print 3 + 2 - 4 % 3 + 1 / 5 + 6
print 3 + 2 < 5 - 7
print 3 + 2 - 4 % 3 + 1.0/5 + 6  #浮点数
print "What's 3 + 2 ?", 3 + 2
print "Is it greater?", 5 > -2

# 中文测试
str = "这是中文"
print str

# 变量命名
cars = 100 #等号两边留空格，代码更易读
space_in_a_car = 4.0
print "There are", cars, "cars available." #cars前后自动加空格

# 打印
my_name = 'Lishuai'
my_eyes = 'blue'
my_hair = 'Brown'
my_age = 35
my_weight = 70.4
print "My name is %s." % my_name  # %s是格式化字符，表示字符串
print "My age is %d." % my_age    # %d 表示整数，%f 表示浮点数， %r 是通用类型，可以用于调试
print "I have %s eyes and %s hair." % (my_eyes, my_hair)
print "My weight is %f , about %d " % (my_weight, round(my_weight)) # round是四舍五入函数

