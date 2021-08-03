'''for i in range(5):
    for j in range(5):
        print("j:", j, sep=" ", end=" ")
    print("i:",i, "\\n", sep=" ")'''

'''for i in range(5):
    for j in range(5):
        print('*',end=" ")
    print()'''

'''for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()'''

'''for i in range(3):
    for j in range(7):
        print('*', end=" ")
    print()'''

'''for i in range(5):
    for j in range(5):
        if j <=i:
            print("*", end= " ")
    print()'''

'''for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

'''for i in range(5):
    for j in range(5):
        if j>= i:
            print("*", end="")
        else:
            print(" " ,end="")
    print()'''

height=int(input("삼각형의 높이를 입력하세요 : "))

for i in range(height):
    for j in range((height-1)*2+1):
        if i <= j-2 and i>=j+2:
            print("*", end="")
        else:
            print("/" ,end="")
    print()

