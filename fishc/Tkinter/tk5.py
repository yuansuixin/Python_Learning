#  button组件

from tkinter import *

def callback():
    var.set('我不信')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('您所下载的影片含有未成年人限制的内容')

textLabel = Label(frame1,
                  textvariable=var,  #显示tkinter的变量
                  justify=LEFT,#  左对齐
                  padx=10)# 边距
textLabel.pack(side=LEFT)

photo = PhotoImage(file='a.png')
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2,text='我已经18了',command=callback)
theButton.pack()
frame2.pack(padx=10,pady=10)
frame1.pack(padx=10,pady=10)
mainloop()





































