from tkinter import *

root = Tk()

LANGS=[('python',1),('Pel',2),('java',4),('Lua',3)]

v = IntVar()

v.set(1)

for lang,num in LANGS:
    b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)
    b.pack(fill=X)# 横向填充

# Radiobutton(root,text='one',variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text='two',variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text='three',variable=v,value=3).pack(anchor=W)
# Radiobutton(root,text='t',variable=v,value=4).pack(anchor=W)

mainloop()




