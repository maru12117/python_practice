#람다표현식(이름이 없는 익명함수)

'''def plus_ten(x):
    return x+10

print(plus_ten(1))'''

'''plus_ten=lambda x: x+10 #x+10을 return한다
print(plus_ten(1))

print((lambda x:x+10)(1)) '''
#변수 사용은 외부를 통해서 사용해야함
'''y=10
print((lambda x: x+y)(1))'''

'''def plus_ten(x):
    return x+10

print(list(map(plus_ten,[1,2,3])))

print(list(map(lambda x: x+10,[1,2,3])))'''
#람다표현식에서 if를 사용했다면, 반드시 else를 사용해야함
'''a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:str(x) if x%3==0 else x,a)))'''


'''a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:str(x) if x==1 else float(x) if x==2 else x+10,a)))'''
'''a = [1,2,3,4,5,6,7,8,9,10]
def fun(a):
    if a==1:
        return str(a)
    elif a==2:
        return float(a)
    else:
        return a+10

print(list(map(fun,a)))'''

'''a = [1,2,3,4,5]
b=[2,4,6,8,10]

print(list(map(lambda x,y: x*y, a,b)))'''

#list(map(f,a))는 주는 리스트를 모두다 가져와라~~!
'''plus_ten = lambda x:x+10
print(lambda x:x+10) #fuction<lambda>
print(plus_ten) #fuction<lambda>

data = plus_ten(1)
print(data) #11

a1 = lambda x:x+10
print(a1(1)) #11


a2 = (lambda x:x+10)(1)
print(a2) #11

y=10
a_10=lambda x:y+10
print(a_10(5)) #20

a = [1,2,3,4,5]
b=[2,4,6,8,10]

a_1 = list(map(lambda x,y: x*y, a,b))
print("a_1", a_1)'''

'''def f(x):
    return x>5 and x<10 #5보다 크고 10보다 작은 것만 걸러지는 메소드 filter

a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(f,a)))
#filer는 결과가 참인 요소만 가져오고 거짓 요소는 버림'''

#간단한 함수 쓸때..
'''a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(lambda x:x>5 and x<10,a)))'''


#reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 후에 누적해서 반환하는 함수
def f(x,y):
    print(x,y) #누적해서 더하기
    return x+y

a=[1,2,3,4,5]
from functools import reduce
reduce(f,a)
#print(reduce(f,a)) #15

a=[1,2,3,4,5]
from functools import reduce
print(reduce(lambda x,y :x+y,a))




























