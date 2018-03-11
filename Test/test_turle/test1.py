import turtle

print('**********************************')
# def square(t):
#     for i in range(4):
#         t.lt(90)
#         t.fd(100)
#
# bob = turtle.Turtle()
# square(bob)
# turtle.mainloop()

print('*****************************************')

# def square(t,length):
#     t = turtle.Turtle()
#     for i in range(4):
#         t.lt(90)
#         t.fd(length)
#     turtle.mainloop()
#
# bob = turtle.Turtle()
# square(bob,20)
# bob.mainloop()

print('*****************画出正n边形*********************')
# length为边长
# def polygon(t,length,n):
#     t = turtle.Turtle()
#     for i in range(n):
#         t.lt(360/n)
#         t.fd(length)
#
# #
# bob = turtle.Turtle()
# polygon(bob, 1, 300)
# turtle.mainloop()
print('******************画圆**********************')
import math
def arc(t, r, angle):
    arc_length = 2* math.pi*r*angle /360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = angle /n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


