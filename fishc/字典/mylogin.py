

print('\t\t\t用户登录程序')
print('=========================================')
print('\t\t新建用户:n')
print('\t\t登录账号:e')
print('\t\t退出程序:q')
print('=========================================')

messages = {}
while 1:
    n = input('请输入指令代码：')

    if n == 'n':
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if not messages:
            for key in messages:
                if key == username:
                    print('用户名已经存在')
                else:
                    messages[username] = password

        messages[username] = password
        print('注册成功，赶紧试试登录吧。')
    # 登录
    elif n == 'e':
        user = input('请输入登录的用户名：')
        pswd = input('请输入密码：')
        for key in messages:
            if user == key:
                if pswd == password:
                    print('欢迎进入xxx系统。')
                else:
                    print('密码错误')
            else:
                print('用户名错误。')
        print('***********************')
    elif n == 'q':
        break
print(messages)
print('程序结束')






