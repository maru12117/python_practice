'''x = {'a':10, 'b':20, 'c':30, 'd':40}
#키와 값쌍을 추가하기
x.setdefault('e',50)
x.setdefault('f')
print(x)

#키값을 수정하기
x.update(b=45,c=98,g=66)
print(x)

x.update(h=56)
print(x)

x.update({'b':102, 'i':987})
print(x)

x.update([['a',56],['c',89]]) #전체 리스트로 map해야함
print(x)

x.update([['a','c'],[56,89]]) #전체 리스트로 map해야함
print(x)

x.update(zip(['a','b'],[89,45])) 
print(x)

#키 삭제하기
x.pop('c') #해당 키를 직접 입력함
print(x.pop(56)) #직접 pop으로 찍으면 해당 값을 반환함
print(x)

del x["i"]
print(x)

#popitem() :튜플 형태로 마지막 키를 반환하고, 해당 키-값을 삭제함

print(x.popitem())
print(x)
print(x.popitem())
print(x)

#x.clear() #그냥 모든 키값들을 삭제함
print(x)

#키를 통해 값을 가져오는 형태!!!(조회?@)

print(x.get('a'))

print(x.items()) #리스트안에 튜플이 들어있는 형식임 dict_items형식...

y=x.items()
print(type(y))'''

#리스트를 딕셔너리로 만들기(키값으로 만들고 값은 모두 None으로 생성함)
a=['a','b','c','d','e','f']
x=dict.fromkeys(a,100)
#print(x) # x라는 dictionary가 생성됨

#반복문을 사용하여 

b={'a':100,'b':20,'c':45,'d':56,'e':67,'f':98}
'''for x in b:
    print(x, end=" ") #키값만 출려됨
print()
for x in b.items():
    print(x, end=" ") #튜플로 출력이됨'''

'''for x,y in b.items():
    print(x,y , end=" ")'''

#키& 값만 출력하기

'''for x in b.keys():
    print(x)
    
for x in b.values():
    print(x)'''

#Dictionary의 표현식 사용하기

'''keys = ['a','b','c','d','e','f']
x = {a:0 for a in dict.fromkeys(keys)}
print(x)


y={a:0 for a in {'a':10,'b':23,"c":56}.values()}
print(y)

#키와 값을 자리 바꾸기
z = {a:b for b,a in {'a':10,'b':23,"c":56}.items()}
print(z)

#딕셔너리의 할당과 복사
a = {'a':0,'b':0,'c':0,'e':0}
b=a
b['a']=5
print(a)
print(b)

a = {'a':0,'b':0,'c':0,'e':0}
b=a.copy()
b['a']=45
print(a)
print(b)

#중첩 Dictionary에서는 deepcopy()를 사용하여 복사함
import copy 
c = {'a':{'python':2.7},'b':{'python':3.6}}
#d=c.deepcopy()
d=copy.deepcopy(c) #deepcopy활용방법
d['a']['python']=5
print(c)
print(d)'''


#

v = {'a':[1,1],'b':[3,3]}

for key, value in v.items():
    print(key, value[0],value[1])


























