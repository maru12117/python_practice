# 세트는 인덱스가 없으며, 출력해보면 무작위로 나옴
'''fruits = {'strawberry','grape','orange', 'pineapple', 'cherry','orange'}
print('orange' not in fruits)'''

'''a = set('apple') #각 문자가 세트단위로 출력됨
print(a)

b= set(range(4))
print(b)'''

#빈 세트만들기 #c={}으로 그냥 만들면 dictionary가 만들어지기 떄문에 주의!
'''c = set()
print(type(c))

a=set("안녕하세요")
print(a)

#세트 안에는 세트를 넣을 수 없으나, frozenset()를 활용하면, 세트안에 넣을 수 있음
b=frozenset({1,2,3,4,5})
d = frozenset({5,62,3,64,65})

e=frozenset({frozenset({1,2,3,4,5}),frozenset({5,62,3,64,65})})
print(e)'''

a = {1,2,3,4,5}
b={5,6,7,8,9}
'''print(a|b) #합집합(중복되는 것은 제외된다!) | 을 사용(union)
print(set.union(a,b))

#교집합 &을 사용 set.intersection
print(a&b)
print(set.intersection(a,b))

#차집합 - 을 사용 set.difference을 사용
print(a-b)
print(set.difference(a,b))

#대칭차집합 ^을 사용 set.symmetric_difference을 사용
print(a^b)
print(set.symmetric_difference(a,b))'''

#다른 세트를 더하기
'''a = {1,2,3,4,5}
a |= {6} #이대로 프린트를 불가능하며, 다시 a를 출력하면..{6}세트가 저장됨
print(a)

a.update({8})
print(a)

#겹치는 세트만 저장하기
c = {1,2,3,4,5}
c &= {3,2,5,10,8,9,11}
print(c) #교집합부분만 다시 c세트에 저장이됨
c.intersection_update({5,89,65,98,2,5})
print(c)'''

#뺀 세트만 남기기
'''d= {1,2,3,4,5}
d-={2,3}
print(d)
d.difference_update({4})
print(d)

#대칭차집합만 남기기 ^ 사용
e = {1,2,3,4,5}
e ^= {3,4,8,9}
print(e) #중복되는 {3,4}만 떨어지고 나머지 부분은 합해짐
e.symmetric_difference_update({5,8,9,10,12,13,15,14})
print(e)'''

#부분집합 및 상위집합인지 확인하기

a = {1,2,3,4,5}
b={1,2,3,4}
c={2,3,5,1,4}
'''a <= {1,2,3,5}
print(a <= {1,2,3,5})
print(a.issubset(b))
print(a.issuperset(b))'''

print(a ==b)
print(a==c)



















