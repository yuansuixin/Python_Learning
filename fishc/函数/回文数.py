# def huiwen(string):
#     length = len(string)
#     if length%2==0:
#         print(11111111)
#         if list(string[:length/2])==list(reversed(string[length/2:])):
#             print('是回文数')
#             return
#         else:
#             print('不是回文数')
#             return
#     if length%2!=0:
#         print(222222222)
#         print(string[:length//2])
#         print(list(reversed(string[length//2+1:])))
#         if list(string[:length//2]) == list(reversed(string[length//2+1:])):
#             print('是回文数')
#             return
#         else:
#             print('不是回文数')
#             return
#
# s = input('请输入一句话')
# huiwen(s)
#
# print('*****************************方法二*************************')
#
# def huiwen2(s):
#     s = list(s)
#     sub = reversed(s)
#     if s == sub:
#         print('是回文数')
#     else:
#         print('不是回文数')
#
#
# print('************************方法三***************')
#
#
# def palindrome(string):
#     length = len(string)
#     last = length-1
#     length //= 2
#     flag = 1
#     for each in range(length):
#         if string[each] != string[last]:
#             flag = 0
#         last -= 1
#
#     if flag == 1:
#         return 1
#     else:
#         return 0
#
# string = input('请输入一句话：')
# if palindrome(string) == 1:
#     print('是回文联!')
# else:
#     print('不是回文联！')
#

print('**********************方法四')

def huiwen4(m):
    if m == 0:
        return ''
    a = m % 10
    m = m // 10
    return str(a)+ str(huiwen4(m))

m = str(12321)
if m == huiwen4(int(m)):
    print('是回文数')
else:
    print('不是回文数')









