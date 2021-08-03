'''def A():
    x=10
    y=100
    def B():
        x=20
        def C():
            nonlocal x #20
            nonlocal y #100
            x = x+30  #50
            y = y+300 #400
            print(x)
            print(y)
        C()
    B()
A()'''

'''x=1
def A():
    x = 10
    def B():
        X=20
        def C():
            global x #전역변수 1
            x = x+30
            print(x) #31 출력
        C()
    B()
A() '''

#클로저 사용하기
'''def calc():
    a=3
    b=5
    def mul_add(x):
        return a*x+b #함수 바깥쪽에있는 지역변수 a,b를 활용하여 a*x+b를 계산하는 mul_add함수를 만든뒤
    return mul_add #mul_add를 반환함

c= calc() #mul_add를 반환하기 떄문에 
print(c(1), c(2), c(3), c(4), c(5)) #x변수는 mul_add에 있기 때문에 그대로 반환함'''
#함수를 둘러싼 환경(지역변수, 코드 등)이 클로버라는 상태로 만들어서 사용이됨
#프로그램의 흐름을 변수에 저장할 수 있고, 데이터를 숨기고싶을떄(만들어진 알고리즘을 숨겨놓기 위해)
#어떤 함수 내에 중첩된 함수여야 한다

'''def calc():
    a=3
    b=5
    return lambda x:a*x+b #람다는 이름이 없는 익명의 함수이고, 클로서는 함수를 둘러싼 환경을 유지했따가 나중에 다시 사용하는 함수를 뜻함
c = calc()
print(c(1), c(2),c(3), c(4),c(5))'''

'''def calc():
    a = 3
    b = 5
    total=0
    def mul_add(x):
        nonlocal total #total이 mud_add외부에 있으므로 값이 변한 상태에서 유지됨
        total = total + a*x+b
        print(total)
    return mul_add

c = calc()
c(1), c(2),c(3), c(4),c(5)'''

'''def calc():
    a = 3
    b = 5
    def mul_add(x):
        total=0 #mul_add내부에 있으면 계속 total=0으로 초기화됨
        total = total + a*x+b
        print(total)
    return mul_add #클로저는 함수 그대로 이름을 유지해야함

c = calc()
c(1), c(2),c(3), c(4),c(5)'''

#클로저의 지역 변수 변경하기
'''def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a*x+b
        print(total)
    return mul_add

c=calc()
c(1)
c(2)

b = calc() #다시 b라는 객체로 인해서 total=0으로 새로 생성
b(3)
print("=============")
print(b(3)) #none으로 찍히는 이유는...return 해준게 없으니 none값으로 나옴'''

#연습문제

'''def counter():
    i = 0
    def count():
        nonlocal i #지역변수 가져오고.
        i += 1 #1을 계속적으로 추가하여 호출 횟수 추가함
        return i #그것을 그대로 return하고
    return count #클로저 함수를 알리기

c= counter()
for i in range(10):
    print(c(), end=" ") #의미없이 10번을 찍는다.'''


    
        

    
















