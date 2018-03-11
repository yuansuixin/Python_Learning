'''
打印2行2列的方格

'''
a = 2
# 第一行
while a:
    a -= 1
    for n in range(2):
        for row in range(5):
            if row % 5 == 0:
                print('+ ', end='')
            print(' - ', end='')
            if (row+1 == 5) and (n+1 == 2):
                print('+ ', end='')
    print()

    # 第2-5行
    for x in range(4):
        for n in range(2):
            for each in range(5):
                if each % 5 == 0:
                    print('| ', end='')
                print('   ', end='')
                if (each + 1 == 5) and (n + 1 == 2):
                    print('| ', end='')
        print()

for n in range(2):
    for row in range(5):
        if row % 5 == 0:
            print('+ ', end='')
        print(' - ', end='')
        if (row+1 == 5) and (n+1 == 2):
            print('+ ', end='')
print()