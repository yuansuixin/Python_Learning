
from tkinter import *

root = Tk()

textLabel = Label(root,
                  text='您所下载的影片含有未成年人限制的内容',
                  justify=LEFT,#  左对齐
                  padx=10)# 边距
textLabel.pack(side=LEFT)

photo = PhotoImage(file='a.png')
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)

mainloop()

















