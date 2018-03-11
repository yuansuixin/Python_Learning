n = 1234567
# a = list(str(n))
# a.reverse()
# print(a)
# for i in a:
#     print(i,end='')

res = 0
tem = n%10
for i in range(len(str(n))+1):
    tem = n%10
    res = res*10 + tem
    n //= 10
    if not n:
        break
print(res)

