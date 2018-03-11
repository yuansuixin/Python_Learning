# class Turtle:
#     def __init__(self, x):
#         self.num = x
#
#
# class Fish:
#     def __init__(self, x):
#         self.num = x
#
#
# class Pool:
#     def __init__(self, x, y):
#         self.turtle = Turtle(x)
#         self.fish = Fish(y)
#
#     def print_num(self):
#         print(self.turtle.num, self.fish.num)
#
#
# pool = Pool(1, 10)
# pool.print_num()

# class Ticket():
#     def __init__(self,weekend = False,child = False):
#         self.exp = 100
#         if weekend:
#             self.inc = 1.2
#         else:
#             self.inc = 1
#         if child:
#             self.discount = 0.5
#         else:
#             self.discount=1
#     def calcPrice(selfs,num):
#         return selfs.exp *selfs.inc*selfs.discount*num
#
#
# adult = Ticket()
# print(adult.calcPrice(1))
#
# import random
#
# x = [0,10]
# y = [0,10]
#
# class Turtle:
#     def __init__(self):
#         # 初始体力
#         self.power = 100
#         # 初始位置随机
#         self.x = random.randint(x[0],x[1])
#         self.y = random.randint(y[0],y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置
#         new_x = self.x+random.choice([1,2,-1,-2])
#         new_y = self.y + random.choice([1,2,-1,-2])
#
#         #检测移动后是否超过场景x轴边界
#         if new_x <x[0]:
#             self.x = x[0] - (new_x-x[0])
#         elif new_x> x[1]:
#             self.x = x[1] - (new_x - x[1])
#         else:
#             self.x = new_x
#
#         if new_y <y[0]:
#             self.y = y[0] - (new_y-y[0])
#         elif new_y> y[1]:
#             self.y = y[1] - (new_y - y[1])
#         else:
#             self.y = new_y
#
#         self.power -= 1
#         return (self.x,self.y)
#
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
#
#
# class Fish:
#     def __init__(self):
#         # 初始位置随机
#         self.x = random.randint(x[0],x[1])
#         self.y = random.randint(y[0],y[1])
#
#     def move(self):
#         # 随机计算方向并移动到新的位置
#         new_x = self.x+random.choice([1,-1])
#         new_y = self.y + random.choice([1,-1])
#
#         #检测移动后是否超过场景x轴边界
#         if new_x <x[0]:
#             self.x = x[0] - (new_x-x[0])
#         elif new_x> x[1]:
#             self.x = x[1] - (new_x - x[1])
#         else:
#             self.x = new_x
#
#         if new_y <y[0]:
#             self.y = y[0] - (new_y-y[0])
#         elif new_y> y[1]:
#             self.y = y[1] - (new_y - y[1])
#         else:
#             self.y = new_y
#
#         return (self.x,self.y)
#
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
#
# while 1:
#     if not len(fish):
#         print('鱼儿都吃完了，游戏结束')
#         break
#     if not turtle.power:
#         print('乌龟体力耗尽，挂掉了')
#         break
#     pos = turtle.move()
#
#     for each in fish[:]:
#         if each.move() == pos:
#             turtle.eat()
#             fish.remove(each)
#             print('有一条鱼鱼被吃掉')

# import math
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
# class Line():
#     def __init__(self,p1,p2):
#         self.x = p1.getX() - p2.getX()
#         self.y = p1.getY() - p2.getY()
#
#         self.len = math.sqrt(self.x**2+self.y**2)
#
#     def getlen(self):
#         return self.len
#
# point = Point(1,1)
# point2 = Point(2,2)
# line = Line(point,point2)
# print(('直线的长度为%.2f')%line.getlen())


# class C:
#     count = 0
#
#
# a = C()
# b = C()
# c = C()
# print(a.count)  # 0
# print(b.count)  # 0
# print(c.count)  # 0
#
# c.count += 10
# print(a.count)  # 0
# print(b.count)  # 0
# print(c.count)  # 10
#
# C.count += 100  # 类对象
# print(a.count)  # 100
# print(b.count)  # 100
# print(c.count)  # 10






# class C:
#     def x(self):
#         print('oooooo')
#
# c = C()
# print(c.x())
# c.x = 1
# print(c.x())


# class Try_int(int):
#     def __add__(self, other):
#         return int(self)+int(other)
#     def __sub__(self, other):
#         return int(self)-int(other)
#
# a = Try_int(3)
# b = Try_int(5)
# print(a+b)  # 8
# print(a-b)  # -2

# class Nint(int):
#     def __radd__(self, other):
#         return int.__sub__(self,other)  # self - other
#
# a = Nint(5)
# b = Nint(3)
# print(a+b)  # 8
# print(1+b)  # 2  实际上是运行的b-1


# class Nint(int):
#     def __sub__(self, other):
#         return int.__sub__(other,self)
#
# a = Nint(5)
# print(3-a)  # -2
#


#
# class C:
#     def __init__(self, size=10):
#         self.size = size
#     def getSize(self):
#         return self.size
#     def setsize(self,value):
#         self.size = value
#     def delSize(self):
#         del self.size
#     x = property(getSize,setsize,delSize)
#
# c = C()
# print(c.x)
# print(c.size)
# c.x = 1
# print(c.size)

class PlugIn(object):
    def __init__(self):
        self._exported_methods = []

    def plugin(self, owner):
        for f in self._exported_methods:
            owner.__dict__[f.__name__] = f

    def plugout(self, owner):
        for f in self._exported_methods:
            del owner.__dict__[f.__name__]


class AFeature(PlugIn):
    def __init__(self):
        super(AFeature, self).__init__()
        self._exported_methods.append(self.get_a_value)

    def get_a_value(self):
        print('a feature.')


class BFeature(PlugIn):
    def __init__(self):
        super(BFeature, self).__init__()
        self._exported_methods.append(self.get_b_value)

    def get_b_value(self):
        print('b feature.')


class Combine: pass


c = Combine()
AFeature().plugin(c)
BFeature().plugin(c)

print(c.get_a_value())
print(c.get_b_value())















