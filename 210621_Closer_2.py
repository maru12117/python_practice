#전역변수 사용하기
'''x=10
def A():
    x=10
    def B():
        global x #전역함수 x=10을 밑의 x=20으로 변경함
        x=20
        print(x)
    B()
    print(x) #10
A()
print(x)'''

#지역변수 사용
'''def A():
    x=10
    def B():
        nonlocal x #바깥함수 x=10을 밑의 x=20으로 변경함
        x=20
        print(x)
    B()
    print(x)
A()'''

#nonlocal 변수 찾는 순서
'''def A():
    x=10
    y=100
    def B():
        x=20
        def C():
            nonlocal x #20
            nonlocal y #100
            x=x+30
            y=y+300
            print(x) #50
            print(y) #400
        C()
        print(x) #50
    B()
    print(x) #10
A()'''
# global로 전역변수 사용하기
'''x=1
def A():
    x=10
    def B():
        x=20
        def C():
            global x
            x= x+30
            print(x) #31 전역변수가 사용되었기 때문에 변함
        C()
        print(x) #20
    B()
    print(x) #10
A()
print(x) #31'''

#클로저
'''def Calc():
    a=3
    b=5
    def mul_add(x):
        return a*x+b
    return mul_add #함수 자체를 반환함

c=Calc()
print(c(1), c(2), c(3), c(4), c(5)) #여기있는게...'''

#lambda로 클로저만들기
'''def Calc():
    a=3
    b=5
    return lambda x:a*x+b #람다 표현식 자체를 반환함

c =Calc()
print(c(1), c(2))'''

#클로저의 지역변수 변경하기
'''def calc():
    a=3
    b=5
    total=0
    def mul_add(x):
        nonlocal total
        total = total + a*x+b
        print(total)
    return mul_add

c=calc()
print(c(1),c(2),c(3)) #x값에 1,2,3을 넣어라'''

#연습문제
'''def counter():
    i=0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=" " ) #c를 10번 출력'''

#심화문제

def countdown(n):
    i=0
    def countprint():
        nonlocal i
        i+=1
        return n-i+1
    return countprint


n= int(input(" : "))
c = countdown(n)
for i in range(n): #10번을 찍을테니 10부터 1까지 찍어
    print(c(), end=" ")

