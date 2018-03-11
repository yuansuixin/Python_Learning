class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a

fibs = Fibs()
for each in fibs:
    if each<20:
        print(each)
    else:
        break



def libs():
    a=0
    b=1
    while True:
        a,b = b,a+b
        yield a

a = libs()
for each in range(10):
    print(next(a))


print('***************************')

b = {i:i%2 ==0 for i in range(10)}
print(b)


a = {i for i in [1,1,2,3,4,5,6,5,5]}
print(a)

print('***********************')
i=0
while i<5:
    print(i)
    i+=1


#
# def LeapYear():
#     L=[]
#     for each in range(1000,2018):
#         if (each%4==0 and each%100!=0) or (each%400==0):
#             print(each)
#             L.append(each)
#     return L
#
# a = LeapYear()
# print(a)

# def myRev(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]
#

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
import math

def issushu(num):
    if num>0:
        if num ==1:
            return False
        if num %2 == 0:
            return False
        for each in range(3,int(math.sqrt(num)+1),2):
            if num % each == 0:
                return False
        return True
    return False

def getsushe(num):
    while True:
        if issushu(num):
            yield num
        num +=1

result = 0
a = getsushe(3)
for each in range(10):
    print(next(a))






















