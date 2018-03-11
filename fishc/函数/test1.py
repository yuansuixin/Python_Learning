# exercise3.2

# def right_justify(s):
#     for each in range(70):
#         print(' ',end='')
#     print(s)
#
# right_justify('monty')


# def do_twice(f,a=3):
#     f(a)
#     f(a)
#
# def print_spam(a):
#     print('span')
#
# do_twice(print_spam)

'''
定义一个名为 do_four 的新函数，其接受一个函数对象和一个值作为实参。调用这
个函数对象四次，将那个值作为形参传递给它。函数体中应该只有两条语句，而
不是四条
'''

def do_four(f,a=3):
    f(f(a))
    f(f(a))

def print_spam(a):
    print('span')

do_four(print_spam)
