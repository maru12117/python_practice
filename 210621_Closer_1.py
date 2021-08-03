#전역(Global)변수 :  함수를 포함하여 스크립트 전체에서 접근할 수 있는 변수를 전역변수라고 함

'''x =10 #전역변수(모든 범위에서 다 출력이 가능하다)
def foo():
    print(x+1) #전역변수 출력

foo()
print(x+2) #전역변수 출력'''

'''def foo():
    x=10 #foo의 지역변수(local변수)임.
    print(x) #10

foo()
print(x) #에러(x=10은 foo()함수 내에서만 사용이 가능함'''

'''x=10 #전역변수
def foo():
    global x #전역변수 x를 사용하겠다고 설정
            #(함수 안에서 전역변수의 값을 변경하려면 global키워드 사용
    x=20
    print(x) #20(foo의 지역변수 출력)
print(x)
foo()
print(x) #20'''

#전역변수가 없는 상태에서도...
'''def foo():
    global x #전역변수 x를 사용하겠다고 설정
            #(함수 안에서 전역변수의 값을 변경하려면 global키워드 사용
    x=20
    print(x) #20(foo의 지역변수 출력)
    
#print(x) #오류
foo()
print(x) #20'''

'''def print_hello():
    hello = 'Hello world!'
    def print_message():
        print(hello)
    print_message()

print_hello()'''


'''def A():
    x=10
    def B():
        print(x)
        #안쪽 함수는....전역에 영향을 주지않음

    B()
    print(x) #10

A()'''
x=20
def A():
    x=10
    def B():
        global x #바로 바깥쪽의 지역변수를 활용한다
        print(x)

    B()
    print(x+1) #10

A()













