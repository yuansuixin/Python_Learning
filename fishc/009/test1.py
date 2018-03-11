# 验证用户密码
times =3
password='hello'

temp=input("请输入密码：")
while times>0:
    if '*' in temp:
        temp=input("密码中不能有*，您还有3次机会，请重新输入:")
        continue
    times-=1
    if temp=='hello':
        print("密码成功，进入程序。。")
        break
    else:
        password=input("密码错误，您还有"+str(times)+"次机会，请重新输入:")








