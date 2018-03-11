# file_name = input('请输入需要打开的文件名')
# f = open(file_name)
# print('文件内容是：')
# for each in f:
#     print(each)

# try:
#     sum = 1 + '1'
#     f = open('adfg.txt')
#     print(f.read())
#     f.close()
# except OSError as reason:
#     print('文件出错了')
#     print(reason)
# except TypeError as r:
#     print('类型出错了')
# except:
#     print('出错了')

#
#
# def showMaxFactor(num):
#     count = num // 2
#     while count>1:
#         if num % count == 0:
#             print('%d最大的约数是%d' % (num, count))
#             break
#         count -= 1
#     else:
#         print('是素数')
#
# num = input('请输入一个数')
# showMaxFactor(num)



# try:
#     int('12')
# except ValueError as reason:
#     print('出错啦')
#     print(reason)
# else:
#     print('没有任何的异常')

# try:
#     with open('data.txt','w') as f:
#         for each in f:
#             print(each)
# except OSError as reason:
#     print('出错啦')
#     print(reason)

# import random
#
# secret = random.randint(1,10)
# print('------------------我爱鱼C工作室------------------')
# try:
#     temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
#     guess = int(temp)
#     while guess != secret:
#         temp = input("哎呀，猜错了，请重新输入吧：")
#         guess = int(temp)
#         if guess == secret:
#             print("我草，你是小甲鱼心里的蛔虫吗？！")
#             print("哼，猜中了也没有奖励！")
#         else:
#             if guess > secret:
#                 print("哥，大了大了~~~")
#             else:
#                 print("嘿，小了，小了~~~")
#     print("游戏结束，不玩啦^_^")
# except ValueError as reason:
#     print('您输入的有误')
#     print(reason)

# try:
#     with open('My_File.txt') as f:
# # 当前文件夹中并不存在"My_File.txt"这个文件T_T
#         print(f.read())
# except OSError as reason:
#     print('出错啦：' + str(reason))
# except NameError as a:
#     print('文件不存在')
#     print(a)


def int_input():
    try:
        n = input('请输入一位整数：')
        n = int(n)
        print(n)
    except ValueError as a:
        print('您输入的不是整数')
        print(a)


















