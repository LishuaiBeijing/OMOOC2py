# -*- coding: utf-8 -*-
##################################
# δ��ɣ���¼����ת���
##################################

## ��ӡ����
x = "There are %d types of people." % 10
y = 5.0
print "I said: %r." % x  # %r����Ĳ��Ǵ�ӡ������������ԭʼ����raw data
print "I said: %r" % y

print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
print end1 + end2 + end3, # ��ӡʱ�ÿո񣬻��һ���ո񣬵��Ǵ�ӡ��һ����
print end4 + end5 + end6
print end1 + end2 + end3  # ȥ�����ţ��Աȴ�ӡ���
print end4 + end5 + end6

months = "Jan\nFeb\nMar\n"
print "Months are %r." % months
print "Months are %s." % months

persian_cat = "I'm \\ a \\ cat." # ��\��ͷ��ת����кܶ࣬��Ҫ��¼�ڱʼ���
fat_cat = """
\t* cat food
\t* fishes
"""
print persian_cat
print fat_cat

## ��ȡ��Ļ����
print "How old are you?", 
age = raw_input()
print "So you are %d years old." % int(age) # raw_input������Ĭ��Ϊstring����

age = raw_input("How old are you?") #�������÷���ͬ
print "So you are %d years old." % int(age) 




