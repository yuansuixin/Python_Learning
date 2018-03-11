list1 = []
def exchang(n):
    result = ''
    if n == 0:
        return result
    else:
        return exchang(n//2) + str(n % 2)
print(exchang(9))

#分解出每位的数字并按照顺序存放到列表里
list1 = []
def get_digits(x):
    a = x % 10
    list1.insert(0, a)
    x = x // 10
    if x == 0:
        return
    else:
        get_digits(x)
    return list1

print(get_digits(123))