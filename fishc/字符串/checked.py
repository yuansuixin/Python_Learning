
#密码安全性检查代码
#
# 低级密码要求：
# 1.密码由单纯的数字或字母组成
# 2.密码长度小于等于8位
#
# 中级密码要求：
# 密码必须要由数字、字母或特殊字符
# 密码长度不能低于8位
#
#高级密码要求：
# 密码必须由数字字母及特殊字符
# 密码只能由字母开头
# 密码长度不能低于16位
#
#

zifu=R'''~!@#$%^&*()_=-/,.<>?;:[]{}\|'''
chars='qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
password=input("请输入需要检查的密码组合：")

length=len(password)

while (password.isspace() or length==0):
    password=input("您输入的密码为空，请重新输入：")
    length=len(password)
#判断长度
if length<=8:
    flag_len=1
elif 16>length>8:
    flag_len=2
else:
    flag_len=3

flag_con=0
#判断是否包含字母
for each in password:
    if each in chars:
        flag_con +=1
        break

#判断是否包含数字
for each in password:
    if each in range(10):
        flag_con+=1
        break

#判断是否包含特殊符号
for each in password:
    if each in zifu:
        flag_con+=1
        break
while 1:
    print("您的密码安全级别评定为：",end=" ")
    if flag_len==1 or flag_con==1:
        print("低")
    elif flag_len==3  and  flag_con==3 and (password[0] in chars):
        print("高")
        print("请继续保持")
        break
    else:
        print("中")
    print("请按照一下方式提升您的密码安全级别：\n\t1.密码必须由数字、字母及特殊字符三种组合\
\n\t2.密码只能由字母开头\n\t3.密码长度不能低于16位")
    break













