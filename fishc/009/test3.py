print("red\tgreen\tyellow")
for red in range(1,4):
    for green in range(1,7):
        for yellow in range(1,4):
            if red + green+ yellow==8:
                print(red,end=" ")
                print(green,end=" ")
                print(yellow,end=" ")
                print()