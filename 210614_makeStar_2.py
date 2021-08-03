'''for i in range(5):
    for j in range(5): #한 줄당 5개씩 출력할거야
        print("j: ",j, sep="", end=" ")
    print("i: ", i, '\\n', sep="" )'''

'''for i in range(5):
    for j in range(5):
        print("*", end="")
    print()'''

'''for i in range(5):
    for j in range(5):
        if i <= j:
            print("*", end=" ")
        else:
            print(' ' ,end=" ")
    print()'''

'''for i in range(1,6):
    for j in range(5-i):
        print('/', end="")
    for j in range(1,i*2,1):
        print("*", end="")
    print("")'''

'''n=5
for i in range(n):
    for j in range(0,i):
        print('/', end=" ")
    for j in range(i,9-i):
        print('*', end= " ")
    print()'''

'''n=int(input(' : '))
for i in range(n):
    for j in range(i):
        print('/' , end=' ')
    for j in range(2*n-2,2*i-1,-1):
        print('*', end=' ')
    print()'''

n=int(input(' : '))
for i in range(n):
    for j in range(n-i):
        print('/' ,end='')
    for j in range(n-1,2*i+2):
        print('*', end=" ")
    print()
