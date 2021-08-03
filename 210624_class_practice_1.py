#클래스 사용하기(클래스는 객체를 표현하기 위한 문법임)

'''class Person:
    def greeting(self): #첫번쨰 매게변수는 반드시 self를 작성해야함
        print("Hello")

james = Person() #Class 명칭인 Person으로 변수 james를 만듦 해당 james는 Person의 인스턴스(instance)임
james.greeting() #Pesron Class에서 greeting 함수를 호출함'''

#인스턴스(instance)=클래스 : 인스턴스.메서드()
#인스턴스를 통해 호출하는 메서드를 인스턴스 메서드라고 부름
#클래스는 특정 개념을 표현만 할뿐, 사용하려면 인스턴스를 생성해야함
#메서드는 클래스에 직접 호출하는 것이 아니라, 객체를 생성한 후 객체를 통해 접근함

#인스턴스를 통해서 호출한다!
'''a = int(10)
print(type(a))

b = [0,1,2]
print(type(b))

c= {'x':10,'y':20}
print(type(c))

maria=Person()
print(type(maria))''' #<class '__main__.Person'>

#보통 객체만 지칭할떄는 객체라고 부르지만, 클래스와 연관지어 말할때는 인스턴스라 함

'''class Person:
    def __init__(self):
        self.hello="안녕하세요 저는 사람입니다." #클래스 자체(자동 생성자) : 자기 자신에 속성을 추가

    def greeting(self): #자기 자신을 호출하면 self임
        print(self.hello)


james = Person()
james.greeting() '''#안녕하세요 저는 사람입니다.

#__init__ 메서드는 james = Person()처럼 클래스에서 ()를 붙야서 인스턴스를 만들떄 호출되는 특별한 메서드임
# 즉, 클래스를 만들때 의지와 상관없이 만들어야 하는 메소드

'''class Person():
    def __init__(self, name, age, address): #자동호출
        self.hello = "안녕하세요"
        self.name1 = name
        self.age1 = age
        self.address1 = address

    def greeting(self):
        print("{0} 저는 {1} 입니다".format(self.hello, self.name1))
        
name=input("이름이 무엇입니까? " )
age=input("나이가 몇살입니까? " )
address=input("주소가 무엇입니까? " )
maria = Person(name, age, address)

name=input("이름이 무엇입니까? " )
age=input("나이가 몇살입니까? " )
address=input("주소가 무엇입니까? " )
james= Person(name, age, address)

maria.greeting() #maria객체로 할때의 greeting()호출
james.greeting() ##james객체로 할때의 greeting()호출

print("첫번째 이름: ",maria.name1)
print("첫번째 나이: ",maria.age1)
print("첫번째 주소: ",maria.address1)
print("두번째 이름: ",james.name1)
print("두번째 나이: ",james.age1)
print("두번째 주소: ",james.address1)'''

#비공개 속성 만들기 __wallet1

'''class Person():
    def __init__(self, name, age, address, wallet): #자동호출
        self.hello = "안녕하세요"
        self.name1 = name
        self.age1 = age
        self.address1 = address
        self.__wallet1=wallet #변수 앞에 __을 붙여서 비공개 속성으로 만듦

maria = Person("마리아",20,"서초동",10000)
maria.__wallet -= 3000 #클래스 바깥에서 비공개 속성에 접근할 경우, 에러가 발생

print("이름: ",maria.name1)
print("나이: ",maria.age1)
print("주소: ",maria.address1)
print("주소: ",maria.wallet1) '''

#비공개 속상 사용하기
'''class Person():
    def __init__(self, name, age, address, wallet): #자동호출
        self.hello = "안녕하세요"
        self.name1 = name
        self.age1 = age
        self.address1 = address
        self.__wallet1=wallet #비공개 속성
        
    def pay(self, amount): #비공개 속서은 클래스안의 메서드에서만 접근할 수 있음
        if amount>self.__wallet1:
            print("돈이 모자르네요!")
            return
        self.__wallet1 -= amount #원래 지갑에서 amount양을 뺸것 
        print("이제 {0}원 남았네요".format(self.__wallet1))

maria = Person("마리아",20,"서초동",10000)
maria.pay(3000) #클래스 바깥에서 비공개 속성에 접근할 경우, 에러가 발생

print("이름: ",maria.name1)
print("나이: ",maria.age1)
print("주소: ",maria.address1)
#print("주소: ",maria.__wallet1)'''  #밖에서 __wallet1을 접근하는 것은 불가능함

#연습문제
'''class Annie():
    def __init__(self, health, mana, ability_power): #자동호출(클래스 내에서 선언해줘야함)
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        tibbers=self.ability_power*0.65+400
        print("티버의 피해량은 %.2f" % tibbers)
        
health, mana, ability_power = map(float,input().split())
x=Annie(health = health, mana=mana, ability_power=ability_power)
x.tibbers()'''

#연습문제
class Orange_Management():
    def __init__(self):
        self.__orange_num = 10
        self.balance_orange()
        
    def __del__(self): #클래스 닫기
        print("class를 종료합니다")

    def add_orange(self, add_num):
        self.__orange_num += add_num
        self.balance_orange()

    def remove_orange(self, remove_num):
        self.__orange_num-= remove_num
        self.balance_orange()

    def orange_zero(self):
        self.__orange_num = 0
        self.balance_orange()

    def balance_orange(self):
        print("현재 오렌지 재고는 %d" % self.__orange_num)
        
orange=Orange_Management(orange_num)

orange_num1=int(input("오렌지를 얼마나 추가하시겠습니까: "))
orange.add_orange(orange_num1)

orange_num2=int(input("오렌지를 얼마나 제거하시겠습니까: "))
orange.remove_orange(orange_num2)
orange.orange_zero()






