#2차원 리스트의 요소에 접근하기
#a = [[10,20],[30,40],[50,60]]

'''print(a[0][0])

print(a[1][1])
print(a[2][1])
a[0][1]=1000
print(a[0][1])'''
#2차원 리스트 for 문으로 출력
'''for x in a:
    for y in x:
        print(y, end=" ")
    print()'''

#2차원 리스트 while문으로 출력
'''i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j], end=" ")
        j+=1
    i += 1
    print()'''

#2차원 리스트 range이용해서 접근
'''for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()'''

'''b = [10,20]
x,y = b
print(x,y)'''

#연습문제
'''a = [[1,2,3],[5,6,7],[8,9,10],[12,13,14]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j], end=" ")
        j+=1
    print()
    i +=1'''

'''for x in range(len(a)):
    for y in range(len(a[x])):
        print(a[x][y], end=" ")
    print()'''


'''c=[3,1,3,2,5]
for x in c:
    b=[]
    for y in range(x):
        b.append(0)
    a.append(b)
print(a)'''

#리스트 표현식 (2차원 리스트)
'''a = [[0 for j in range(2)] for i in range(4)]
print(a)'''
b=[3,1,3,2,5]
a = [[0 for j in range(i)] for i in b]
#print(a)
a= [[0]*i for i in b]
print(a)




    







