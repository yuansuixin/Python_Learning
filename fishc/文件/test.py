
#
# f = open('something.txt','w')
# f.write(input('请输入内容。'))
# f.close()

# f1 = open('something.txt')
# f2 = open('something2.txt')
# lines = 0
# if f1 == f2:
#     print('是同一个文件')
# else:
#     for i in f1:
#         for j in f2:
#             lines += 1
#             # print(f1.readline()+'\tf1')
#             # print(f2.readline()+'\tf2')
#             if f1.readline() == f2.readline():
#                 continue
#             else:
#                 print('第'+str(lines)+ '行不一样')
#

# f = open('something.txt')
# L = list(f)
# a = 2
# b = 4
# print('文件的内容如下：')
# # print(L[a:b])
# for i in L[a:b]:
#     print(i,end='')
# # print(L)
# f.close()

timer = 0
f = open('something.txt', 'rt+')
# print(f.read())
for i in f.read():
    if i == 'd':
        timer += 1
print('文件共有'+str(timer)+'个d')
s = input('你确定替换吗，1或0：')
L = []
if s:
    L = list(f)
    print(L)
    for i in L:
        if i == 'd':
            i = '0'
    print('替换成功')
print(L)
print(f.read())
f.close()












