# -*- coding: utf-8 -*-

###################
## �������Է��ض��ֵ����Ҫע��˳��
###################
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)
#print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

###################
## �Զ����ļ��ĵ���
###################
import ex25
sentence = "All good things come to those who wait."

words = ex25.break_words(sentence)
print words

sorted_words = ex25.sort_words(words)
print sorted_words

ex25.print_first_word(words)
print words  #pop(0)��ѵ�һ��Ԫ������б�
ex25.print_last_word(words)
print words  #pop(-1)������һ��Ԫ������б�
