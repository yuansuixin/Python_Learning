import  random
times = 3
secret=random.randint(1,10)
print('---------我爱小甲鱼----------')
guess=0
print('不妨猜一下小甲鱼心里想的是那个数字：',end='')
while (times>0) and (guess !=secret):
    temp = input()
    num=int (temp)
    times-=1
    if guess==secret:
        print("大了")
    else:
        if guess>secret:
            print("猜对了")
        else:
            print("小了")
        if times>0:
            print("再试一次吧",end="")
        else:
            print("机会用完了")
print("game over")
