

from tkinter import *

root = Tk()

GIRLS = ['西施','小甲鱼','貂蝉','王昭君','杨玉环']
v = []
for girl in GIRLS:
    v.append(IntVar())  # 整形的tk变量
    b = Checkbutton(root,text=girl,variable=v[-1])
    b.pack(anchor=W)  # 左对齐


mainloop()