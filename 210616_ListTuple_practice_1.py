'''a = [10,20,30]
a.append(500)
print(a)
print(len(a))'''
#맨 끝에 집어넣는 append
'''a = []
for i in range(10):
    a.append(i)
print(a)'''

'''a=[]
for i in range(10):
    a.append((i+1)*10)
print(a)'''

#확장 extend
'''a = [10,20,30]
a.extend([700,988])
print(a)
print(len(a))'''

#인덱스를 활용하여 정해진 자리에 삽입 insert(인덱스, 요소)
'''a=[10,20,30]
a.insert(1,[500,600]) #append의 느낌이나네
print(a)

b=[10,20,30]
b[1:1]=[500,600] #extend의 느낌이 나고...
print(b)'''

#삭제하기 popO(), remove()
'''a=[10,20,30] #맨 끝의 것을 삭제하고

a.pop(2) #해당 인덱스의 값이 사라진다(del의 의미를 갖는다)
print(a)

b=[10,20,30]
del b[2] 
print(b)

c = [10,20,30,40, 50, 60]
c.remove(30)
print(c) #20의 값이 사라짐'''

#리스트로 스택만들기(스택 구조: 가장 나중에 들어온 것을 맨 처음에 처리함)

'''a =[]
a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
a.append(40)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)'''

#큐 만들기(큐 구조 : 가장 먼저 들어온 것이 가장 먼저 Out됨)
'''b=[]
b.append(10)
print(b)
b.append(20)
print(b)
b.append(30)
print(b)
b.append(40)
print(b)
b.pop(0)
print(b)
b.pop(0) #b.pop(0) 인덱스를 사용하여 가장 먼저의 인덱스가 삭제될 수 있도록 함
print(b)

a=[10,20,30,40,50,60]

print(a.index(40)) #인덱스를 구한다'''

#20인 인덱스 구하기
'''a=[10,20,30,40,20,50,20,30,60,70,20]
i=0
results=[]
while True:
    if 20 in a:
        nm=a.index(20) #20인 인덱스를 추출함
        results.append(nm+i)
        a.pop(nm) #해당 인덱스를 삭제함
        i+=1
    else:
        break
print(results)'''

a=[10,20,30,40,20,50,20,30,60,70,20]
index_list=[]
while 20 in a:
    indexNum=a.index(20)
    index_list.append(indexNum)
    a[indexNum]="X" #바꿈
print(index_list)
    


        
        
    





