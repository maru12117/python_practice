#2차원 리스트 활용하기
from pprint import pprint #맞춤 출력하기
import copy
#a = [[10,103],[30,40],[50,215],[70,80,90],[100,102,103,105,106]]
'''print(a)
print(sorted(a, key=lambda a: a[1]))'''
'''pprint(a, indent=10, width=20) #들여쓰기...가로폭 20 맞춤

for x,y in a:
    print(x, y)

for x in a:
    for y in x:
        print(y)'''

'''for x in range(len(a)): #len(a)=4(0~3)
    for y in range(len(a[x])): #a[0] 안에 있는 내용만 출력함
         print(a[x][y], end=" ")
    print()'''

'''i=0
while i<len(a):
    x,y=a[i]
    print(x,y)
    i+=1'''
'''i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j], end=" ")
        j+=1
    print()
    i+=1'''

'''a = []
for x in range(3): #세로 3개
    bin_List=[]
    for y in range(3): #가로 3개
        bin_List.append(y)
    a.append(bin_List)
print(a)'''
'''a = [[10,103],[30,40],[50,215],[70,80,90],[100,102,103,105,106]]
b=copy.deepcopy(a)
b[1][0]=98
print(a)
print(b)'''

a = [[10,103],[30,40],[50,215],[70,80,90],[100,102,103,105,106]]
'''for x in range(len(a)): 
    for y in range(len(a[x])):
        print(a[x][y], end=" ")'''


#리스트 표현식 연습문제
b = [[[0]*3 for x in range(4)] for y in range(2)]
print(b)

