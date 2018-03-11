list1 = []
list2=[]
list1 = list(filter(lambda x: (x % 3), range(100)))

print([ each for each in range(100) if each%3==0])


for each in range(100):
    if each not in list1:
        list2.append(each)


print([ i for i in range(1, 100) if not(i%3)])



def power(x, y):
    if y == 1:
        return x
    else:
        return x*power(x, y-1)

print(power(2,3))
