'''a={1,2,3,4}

print(a.isdisjoint({5,6,7,8})) #a에 해당 세트가 겹쳐지지 않는 지 확인
print(a.issubset({3,4})) #해당 세트가 a세트보다 상위의 세트인지 물어보는 것

#subset(작은 단위이니?)  supperset(큰 단위이이니??)라고 물어보는 것!

a.add(5)
print(a)
a.update({6})
print(a)
a.remove(4)
print(a)
a.difference_update({5})
print(a)

a.discard(3)
print(a)
a.discard(4)
print(a)

a.pop()
print(a)'''

#세트 표현식
'''a = {1,2,3,4,5,6,7,8,9}
for x in a:
    print(x, end=" ")
print()

b = {i for i in 'apple'}
print(b)


#if조건문을 활용하여 세트 표현하기
c = {i for i in 'apple pineapple' if i not in 'ale'}
print(c)


d = {1,2,3}
e = {3,4,5}

print(set.difference(e,d))'''


#연습문제 : 공배수 구하기
'''a = {i for i in range(1,100) if i%3==0}
b = {i for i in range(1,100) if i%5==0}
print(a&b)'''

#심사문제 : 공약수 구하기

num1, num2=map(int,input("두개의 양의 정수를 입력하세요 ").split())

#약수 만들기(자신의 밑에있는 것들이 자기 자신을 나누었을떄 0으로 되는 것이 
a={i for i in range(1,num1+1) if num1%i==0}
b={i for i in range(1,num2+1) if num2%i==0}
total=0
for x in a&b:
    total += x
print(total)



















