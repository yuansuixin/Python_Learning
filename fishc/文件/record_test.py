

import codecs

count = 1

f = codecs.open('record.txt', 'rb', 'gbk')
boy = codecs.open('boy.txt','wb','gbk')
girl = codecs.open('gril.txt','wb','gbk')
for each in f:
    if each[:6] != '======':
        (role,spoken) = each.split(':',1)
        if role == '小甲鱼':
            boy.write(spoken)
        if role == '小客服':
            girl.write(spoken)
f.close()
boy.close()
girl.close()






















# for each in f:
#     L = f.readline()
#     if L[:3] == '小客服':
#         print(L, end='')
#         L = L[4:]
#     else:
#         continue