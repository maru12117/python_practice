#range는 +연산자로 객체 연결이 불가능함
'''a=tuple(range(0,10)) + tuple(range(10,20))
print(a)'''
#문자열은 +연산자로 객체 연결이 가능함
'''print('hello' + 'world')'''

'''print([0,10,20,30]*3)'''

#range 또한 * 연산자로 객체 연결이 불가능함
'''print(list(range(0,5,2))*3)
print(tuple(range(0,5,2))*3)

print('Generation'*3)'''


#len 함수
'''a = [0,10,20,30,40,50,60,70,80,90]
print(len(a))

b =(38,76,43,62,19)
print(len(b))

c= range(10)
print(len(c))'''

'''fru1 = ["사과","배","귤","오렌지"]
fru2 = ["토마토","바나나","수박"]
fru = fru1+fru2
print(fru)
print(len(fru))'''

'''print(len(range(0,10,2)))'''

hello = "Hello, world!"
'''print(len(hello))'''

#인덱스 공부하기
#시퀀스 객체의 각 요소는 순서가 정해져있으며, 이 '순서'를 인덱스라고 지칭함
a =[38,21,53,62,19]
'''print(a[0])
print(a[2])
print(a[4])'''

b = (38,21,53,62,19)
'''print(b[0])'''

r = range(0,10,2)
'''print(r[2])'''
'''print(hello[2])'''

'''a = list(range(1,20,2))
print(a)
print(a[2])'''

a =[38,21,53,62,19]
'''print(a[-1])
print(a[-5])'''

b = (38,21,53,62,19)
'''print(b[-1])'''


r = range(0,10,2)
'''print(list(r))
print(r[-3])'''

hello = "Hello, world!"
'''print(list(hello))
print(hello[-4])'''

'''a = list(range(2,101,2))'''
'''print(a[-3])'''

#a(len[a]-1)를 활요하여 마지막 인덱스 순서를 모를때 활용이 가능함
'''print(a[5])'''
'''print(type(len(a)))
print(a[len(a)-1])'''

#요소에 값을 할당하기
d = [0,0,0,0,0,0,0]
d[0]=28
d[1]=21
d[2]=53
d[3]=62
d[4]=19

'''print(d)
print(d[0])'''
#tuple 객체, range, 문자열은 아이템을 할당(값을 지정)할 수 없다
'''e = (0,0,0,0,0,0)
b[0]=2
print(e)'''

'''r = range(0,10,2)
r[0]=3
print(r[0])'''

'''hello = "Hello, world!"
hello[0] = 'A'
print(hello[0])'''

#리스트 삭제하기
'''a =[38,21,53,62,19]
del a[2]
print(a)'''

#튜플, 문자열 range는 읽기전용이기 때문에, 수정 및 삭제가 불가능함
b = (38,21,53,62,19)
'''del b[0]
print(b)''''
















