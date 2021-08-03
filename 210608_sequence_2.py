'''a = (48)
print(type(a))

a = tuple(range(0,10))
print(a)'''

'''b = tuple(range(5,12))
print(b)'''

'''c = tuple(range(-4,10,2))
print(c)'''

'''a = tuple(range(5))
b = tuple(range(5,10,2))
print(a+b)'''

'''b = (4,5,6)
print(list(b))
b = tuple(b)
print(b)'''

'''print(list('Hello'))
print(tuple('Hello'))'''


#리스트와 튜플에 요소를 변수 여러 개에 할당하는 것을 리스트 언패킹(list unpacking)이라고 한다
x=[1,2,3]
a,b,c = x
print(a,b,c)

y=(4,5,6)
d,e,f = y
print(d,e,f)
