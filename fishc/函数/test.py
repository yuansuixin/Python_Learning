# def findstr(s, sub):
#     length = len(s)
#     if length and len(sub):
#         print('您没有输入字符串')
#     times=0
#     for each in range(length-1):
#         if s[each] == sub[0]:
#             if s[each+1] == sub[1]:
#                 times+=1
#                 each = each+1
#
#     print(times)
#
# s = input('请输入目标字符串：')
# sub = input('请输入子字符串（两个字符）：')
# findstr(s,sub)

# print('#########################################')
# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return age(n-1)+2
#
# print(age(5))