'''for x in range(1,6):
    print('*'*x)'''

'''for i in range(5):
    for j in range(5):
        print('*', end=" ")
    print()'''

'''for i in range(5):
    for j in range(5):
        print('j:',j, sep=" ", end=" ")
    print("i:",i,'\\n',sep=" ")'''

'''for i in range(5):
    for j in range(i+1):
        if i >= j:
            print('*', end=" ")
    print()'''

'''for i in range(3):
    for j in range(7):
        print('*', end=" ")
    print()'''

'''for i in range(5):
    for j in range(i+1):
        if i==j:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()'''

'''for i in range(5):
    print('*'*(i+1))'''
# 어렵다
'''for i in range(1,5):
    for j in range(5-i):
        print("b" ,end = " ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()'''
#위에꺼 단순 for 루프를 이용하여 활용함
'''num = 4
for i in range(1,num+1):
    print(" " *(num-i)+"*"*(2*i-1))'''

for i in range(5):
    for j in range(5):
        if i <=j:
            print("*", end=" ")
        else:
            print(" " , end=" ")
    print()

'''n = int(input(" : "))
for i in range(n,0,-1):
    for j in range(n-1):
        print("b", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()'''





    






        
