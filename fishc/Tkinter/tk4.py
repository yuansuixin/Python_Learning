# Label组件
from tkinter import *

root = Tk()

photo = PhotoImage(file='a.png')
theLabel = Label(root,
                 text='学python',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,# 文字正上方显示
                 font=('宋体',20),#设置字体和大小
                 fg='white') #前景色
theLabel.pack()
mainloop()

















