#a = [38,21,53,62,19]

'''print(min(a)) #최소값 구하기
print(max(a)) #최대값 구하기'''

#b= [10,10,10,10,10]
'''total=0
for x in b:
    total = total+x
print(total)
print(sum(b))'''

'''numbers=[]
for x in range(1,11):
    numbers.append(x)
    if x%2!=0:
        numbers.remove(x)
print(numbers)

numbers.insert(0,20) #삽입함
print(numbers)

numbers.remove(20)
print(numbers)

numbers.index(4)
print(numbers.index(4))

numbers.sort(reverse=True)
print(numbers)'''

#리스트 표현식(리스트 안에 for 반복문과 if 조건문을 사용할 수 있음
#range(10)으로 0부터 9까지 생성하여 변수 i에 숫자를 꺼내고, 최종적으로 i를 이용하여 리스트를 만듦
'''a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)'''
#for 반복문 뒤에 if 조건문을 지정하면 숫자를 생성한 뒤 if 조건문에서 특정 숫자만 뽑아내서 리스트를 생성함
'''c = [i for i in range(10) if i%2==0]
print(c)'''

'''d = [i for i in range(6,15) if i%2==0]
print(d)
#따로 연산해서 i에 추가로 연산하는 것도 가능함
f = [i+5 for i in range(10) if i%2==1]
print(f)'''


a = [i*j for i in range(2,10)
         for j in range(1,10) ] #가독성을 위한 들여쓰기
#print(a)

'''b= [1.2,2.5,3.7,4.6]
for x in range(len(b)):
    b[x] =int(b[x])
print(b)'''

#mapping 하기
#매번 for 반복문으로 반복하면서 요소를 변환하려니 조금 번거롭기 때문에, map을 사용하면 편리함
b= [1.2,2.5,3.7,4.6]
b = list(map(int,b))
#print(b)

c = list(map(str,range(10))) #리스트를 출력하면, str타입의 값을 확인할 수 있음
#print(c)

d = list(map(int,"12345"))
#print(d)

e = list(map(float,"12345"))
#print(e)

f = list(map(str,"12345"))
#print(f)

g=map(int,input().split())
#맵 객체는 이터레이터(하나씩 변환하는 )라서 변수 여러 개에 저장하는 unpacking이 가능함

x = input("구른다 : ").split()
m = map(int,x)
l,q = m
print(l)

























