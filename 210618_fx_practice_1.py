
'''def hello(): #함수 선언
    print("Hello, world")

for x in range(10):
    hello() #해당 함수를 실행함'''

'''def add(a,b): #2개의 '매개변수'를 받을거니, a,b를 넘겨줘라.
    print(a + b)

add(10,20) #함수 호출할 때 넣는 값을, '인수'라고 함'''

'''def add(a,b):
    
    return a+b #return을 활용하면 

x = add(10, 20) #return으로 인해 함수 밖의 값으로 x로 들어간다
print(x)'''

'''def add(a,b):
    
    return a+b

print(add(10,20))'''



'''def tripleX(a,b,c):
    return a*b*c
a,b,c=map(int,input(" : ").split())
print(a,b,c)
print(tripleX(a,b,c))'''

'''def add_sub(a,b):
    return a+b, a-b

x=add_sub(10,6) 
print(x) #튜플이 된다(즉, 튜플이 변수 여러 개에 할당되는 특성을 이용한 것)
print(type(x))'''


'''def math(a,b):
    plus = a+b
    minus=a-b
    gop =a*b
    nanugi =a/b
    return plus, minus, gop, nanugi

result1,result2, result3, result4 =math(10,20)
#print("+= {0:.2f} -= {1:.2f} *= {2:.2f} /= {3:.2f}".format(result1,result2, result3, result4))
print("+= %.2f -= %.2f *= %.2f /= %.2f" % (result1,result2, result3, result4))'''

'''def mul(a,b): #add() 함수 내에 있는 mul()함수를 활용함
    c=a*b
    return c

def add(a,b):
    c = a+b
    print(c)
    d = mul(a,b)
    print(d)

x =10
y=20
add(x,y)'''

'''x =10
y=3

def get_quotient_remainder(x,y):
    a=x//y #몫만 구하기
    b=x%y  #나머지 구하기
    return a,b

quotient, remainder =get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))'''

'''x,y = map(int,input().split())
def calc(x,y):
    return x+y, x-y, x*y, x/y

a,s,m,d = calc(x,y)
print('덧셈: {0}, 뺼셈:{1}, 곱셈:{2}, 나눗셈:{3}'.format(a,s,m,d))'''









