# -*- coding:utf-8 -*-
# title:简单日记软件
# description: 支持日记写入，支持日记输出
# layout: 主界面是日记显示界面，按钮1--写入日记，点击后弹出对话框，写入日记，点击确定后保存，按钮2--退出软件
# extention: 
#    1.支持简单的版本控制，可以回溯此前的N个版本  
#    2.直接改造成一个界面，与记事本类似，显示已有日记，并直接续写，设置保存和回退按钮（这跟记事本不是一样了？ ）

import Tkinter as tk

class Diary:
    def __init__(self , master):
        frame = tk.Frame(master , width=300, height=400 , bg="" , colormap="new")
        frame.pack()

        '''
        self.button = tk.Button(frame , text="Quit" , fg="red" , command=frame.quit)
        self.button.pack(side=tk.LEFT)
        
        self.hi_there = tk.Button(frame , text="Hello" , command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)'''

    def say_hi(self):
        input_str = raw_input(" > ")
        print input_str

if __name__=='__main__':
	root = tk.Tk()
	diary = Diary(root)
	root.mainloop()


