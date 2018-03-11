import turtle

bob = turtle.Turtle()  # 创建一个窗口
print(bob)

bob.fd(100)  # 向前走
bob.lt(90)  # 左转
bob.fd(100)

for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()  # 等待用户操作





