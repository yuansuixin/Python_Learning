# import easygui
# import random
#
# secret = random.randint(1,10)
# print('------------------我爱鱼C工作室------------------')
# try:
#     temp = easygui.enterbox("不妨猜一下小甲鱼现在心里想的是哪个数字：")
#     guess = int(temp)
#     while guess != secret:
#         temp = easygui.enterbox("哎呀，猜错了，请重新输入吧：")
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



# import easygui
#
# msg = '请填写一下联系方式'
# title='账号中心'
# fieldNames = ['*用户名','*真实名字','固定电话','*手机号码','QQ号码','*E-mail']
# fieldValues = []
# fieldValues = easygui.multenterbox(msg,title,fieldNames)
#
# while 1:
#     if fieldValues == None:
#         break
#     errmsg = ''
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == '' and option[0] == '*':
#             errmsg += ('[%s]为必填项\n\n'%fieldNames[i])
#         if errmsg == '':
#             break
#         fieldValues = easygui.multenterbox(errmsg,title,fieldNames,fieldValues)
#
# print('用户资料如下：%s'%str(fieldValues))

# import easygui
# import os
#
# file_path = easygui.fileopenbox(default='*.txt')
#
# with open(file_path) as old_file:
#     title = os.path.basename(file_path)
#     msg = '文件%s的内容如下：' % title
#     text = old_file.read()
#     text_after = easygui.textbox(msg, title, text)
#
# if text != text_after[:-1]:
#     choice = easygui.buttonbox('检测到文件内容发生变化，请选择以下操作：'
#                                , '警告', ('覆盖保存', '放弃保存', '另存为'))
#     if choice == '覆盖保存':
#         with open(file_path, 'w') as old_file:
#             old_file.write(text_after[:-1])
#     if choice == '放弃保存':
#         pass
#     if choice == '另存为':
#         another_path = easygui.filesavebox(default='.txt')
#         if os.path.splitext(another_path)[1] != '.txt':
#             another_path += '.txt'
#         with open(another_path, 'w') as new_file:
#             new_file.write(text_after[:-1])









import easygui as g
import os


def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines)
    title = '统计结果'
    msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total / 1000, 100000 - total)
    g.textbox(msg, title, text)


def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s ...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass  # 不可避免会遇到格式不兼容的文件，这里忽略掉......
    return lines


def search_file(start_dir):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            lines = calc_code(each_file)  # 统计行数
            # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
            # 统计文件数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines

        if os.path.isdir(each_file):
            search_file(each_file)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
file_list = {}
source_list = {}

g.msgbox("请打开您存放所有代码的文件夹......", "统计代码量")
path = g.diropenbox("请选择您的代码库：")

search_file(path)
show_result(path)














