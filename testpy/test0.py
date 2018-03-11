"""
笔试题目
"""
#
print('**************1.对数组进行去重的操作，***************')
# 方法一
L = [1,2,3,2,4,5,3,7]
a = []
for i in L:
    if i not in a:
        a.append(i)
print(a)

# 方法二
a = set(L)
print(a)

# 方法三：
d = {}
a = d.fromkeys(L).keys()
print(a)

#
print('**************2.python 的异常处理机制，并打印到日志中，***************')
# import logging
#
# try:
#     a = 2
#     b=0
#     c = a/b
# except ZeroDivisionError as s:
#     logging.error('分母为0')


print('*************3. 现有一个test.txt文件，使用Python逐行读取其中的数据****************')
with open('abc.txt','r') as f:
    while f:
        a = f.readline()
        print(a,end='')
        if not a:
            break
print()


print('*****************************4.使用Python随机生成1-10000之间的数')
import random

a = random.randrange(1,10001)
print(a)

print('*************5.使用Python对字典中的数据进行遍历****************')
d = {}
for i in range(1,6):
    d[i] = '红'+str(i)
print(d)

for key,value in d.items():
    print('key={},value={}'.format(key,value))

for each in d:
    print(each,'---->',d[each])

print('*************6.实现200万并发请求****************')
# import time
# from multiprocessing import Process,Pool
# def fn(*args):
#     print('fn开始了',args)
#     a = time.time()
#     time.sleep(1)
#     print('*************',args,time.time()-a)
#     print('fn结束')
#
# def main():
#     print('gogogo')
#     pool = Pool()
#     for i in range(20):
#         pool.apply_async(fn,args=('process'+str(i),12))
#
#     pool.close()
#     pool.join()
#     print('****************')
#
# if __name__ == '__main__':
#     main()
# import time
# import threading
# def love():
#     print('love开始了',threading.current_thread().name)
#     time.sleep(1)
#     print('love结束了*****************',threading.current_thread().name)
#
#
# def main():
#     print('gogogoog')
#     a = threading.Thread(target=love,name='green')
#     b = threading.Thread(target=love,name='red')
#
#     a.start()
#     b.start()
#     a.join()
#     b.join()
#     print('***************888888')
#
#
# if __name__ == '__main__':
#     main()
print('*************7.冒泡排序****************')
L = [1,5,2,23,9,3]
for i in range(len(L)-1):
    for j in range(len(L)-1-i):
        if L[j] >L[j+1]:
            L[j],L[j+1] = L[j+1],L[j]
print(L)

print('*************8.选择排序****************')

for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        if L[i] >L[j]:
            L[i],L[j] = L[j],L[i]
print(L)

print('*************8.****************')
a0={'a':1,'b':2,'c':3,'d':4,'e':5}
a1=0,1,2,3,4,5,6,7,8,9
a2 = 1,2,3,4,5
a3 = [a0[s] for s in a0]
print(a3) # 1，2，3，4，5
a4 = 1,2,3,4,5
a5 = 0,1,4,9,16,25,36,49,64,81
a6 = [[i,i*i] for i in a1]
print(a6) #[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

print('*************8.(2)****************')
[0,1]
[3,2,1,0,1,4]
[0,1,4]

print('*************10.****************')

# import pymysql
# db = pymysql.connect('localhost','root','123456','qf')
# cursor = db.cursor()
# sql = 'select count(id) from stu'
# cursor.execute(sql)
# a = cursor.fetchall()
# print(a)
# cursor.close()
# db.close()

print('*************4.****************')
b = 'abcdefg'
a = b[4:]
print(a)
print('*************5.****************')
# 占位
print('*************7.****************')
# import calendar
# print(calendar.calendar(2017))

import calendar

month_day = {1: 31,
             2: 28,
             3: 31,
             4: 30,
             5: 31,
             6: 30,
             7: 31,
             8: 31,
             9: 30,
             10: 31,
             11: 30,
             12: 31}

year = input('请输入年份，展示全年的日期：')
if calendar.isleap(int(year)):
    month_day[2] = 29

for key,value in month_day.items():
        for i in range(1,value+1):
            print('{}-{}-{}'.format(year,key,i))

print('**********v***7.****************')






