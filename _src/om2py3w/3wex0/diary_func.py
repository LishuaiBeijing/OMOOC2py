# -*-coding=utf-8 -*-


def inputdiary(file):
    print "逐行输入日记(exit表示结束输入)：\n"
    diary_input = ""
    while 1:
        line = raw_input(" > ")
        if line=="exit":
            file.write(diary_input)
            exit(0)
        else:
            diary_input = diary_input + line + "\n"

def printdiary(file):
    print "日记：\n"
    diary = file.read()
    print diary

if __name__=='__main__':
    #输入日记
    diary_file = open("diary",'a')
    inputdiary(diary_file)
    diary_file.close()
    #输出日记
    diary_file = open("diary",'r')
    printdiary(diary_file)
    diary_file.close()
