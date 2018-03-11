'''

题目内容：

两位整数相乘形成的最大回文数是 9009 = 99 × 91。编写程序，求得任意输入的 n 位整数相乘形成的最大回文数。



输入格式:

正整数 n



输出格式：

n 位整数相乘形成的最大回文数



输入样例：

2
输出样例：

9009
'''


def huiwen(n):
    n = list(n)
    m = list(reversed(n))
    if m == n:
        return n
    return -1


def main():
    n = '2'
    x = int((int(n))*'9')
    for i in range(x*x,0,-1):
        a = huiwen(str(i))
        if list(str(i)) == a:
            print(i)
            break






if __name__ == '__main__':
    main()




























