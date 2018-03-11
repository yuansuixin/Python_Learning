def Fibr(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return Fibr(n-1)+Fibr(n-2)

a = Fibr(12)
print(a)