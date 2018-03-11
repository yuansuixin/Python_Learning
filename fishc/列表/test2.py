
list1=[ (x,y) for x in range(10) for y in range(10)  if x%2==0 if y%2!=0]

print(list1)

##########################################################

list2=[]
list3=[]
for x in range(10):
    if x %2 ==0:
        list2.append(x)
    for y in range(10):
        if y%2!=0:
            list3.append(y)
for x in list2:
    for y in list3:
        print(x,',',y,end="\t")

###################################
print()
list4=[]
for x in range(10):
    for y in range(10):
        if x%2==0:
            if y%2!=0:
                list4.append((x,y))
print(list4)