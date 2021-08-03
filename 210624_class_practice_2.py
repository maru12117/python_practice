#비공개 메서드
'''class Person():
    def __init__(self):
        self.hello="안녕하세요"
        self.__print()

    def __print(self):
        print(self.hello)

james = Person()''' #인스탄스 생성

#연습문제(캐릭터)
    
'''class Knight():
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print("베기 출력")


x=Knight(health=542.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()'''

#클래스 자체의 속성을 사용하기
'''class Person():
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff) #bag 리스트에 stuff를 집어넣음

james = Person()
james.put_bag("책")

maria = Person()
maria.put_bag("열쇠")

print(james.bag) 
print(maria.bag)'''

'''class Person():
    bag = [] #클래스 속성이기 떄문에 모든 가방을 공유함
    #따라서 인스턴스 속성으로 만들면 가방을 공유하지 않음

    def put_bag(self, stuff):
        Person.bag.append(stuff) #조금더 명확하게 하기 위해 Person(클래스 이름)으로 클래스 속성에 접근함
        
james = Person()
james.put_bag("책")

maria = Person()
maria.put_bag("열쇠")

print(Person.bag) 
print(Person.bag)'''

'''class Person():
    def __init__(self):
        self.bag=[] #인스턴스 속성으로 가방을 만듦

    def put_bag(self, stuff):
        self.bag.append(stuff)
        
james = Person()
james.put_bag("책")

maria = Person()
maria.put_bag("열쇠")

print("제임스", james.bag) 
print("마리아",maria.bag)'''

'''class Knight():
    __item_limit=10

    def print_item_limit(self):
        print(self.__item_limit) #10

garen=Knight()
garen.print_item_limit() 

print(Knight.__item_limit) #에러 발생(비공개 속성)'''

#정적메소드 @staticmethod (인스탄스가 필요없음) 바로 클래스에서 사용함
'''class Calc:
    @staticmethod #정적메소드 (self를 사용하지않음)
    def add(a,b):
        return a+b #리턴쓰면 객체로 받아야지.

    @staticmethod
    def mul(a,b):
        print(a*b)

d=Calc.add(10,20) #인스탄스를 생성하지않고, 바로 클래스에서 메서드를 호출함
print(d)
Calc.mul(10,20) #순수함수일때, 즉 인스턴스의 영향을 끼치지않고, 순수하게 결과만을 요구할때 정적 메소드(staticmethod를 사용함)
'''

#클래스 메소드 @classmethod

'''class Person():
    count=0

    def __init__(self):
        Person.count+=1 #인스턴스가 만들어질때 count로 하나씩 추가함


    @classmethod
    def print_count(cls):
        print("{0} 명 생성되었습니다".format(Person.count))

james=Person()
maria = Person()

Person.print_count() #호출함'''

#틀린문제
'''class Person():
    x= [3,5,6,7]

print(Person.x) #클래스 자체로 그냥 진행'''

#연습문제
'''class Date():
    @staticmethod
    def is_date_valid(date):
        date=date.split("-")
        if 1<=int(date[1])<=12 and 1<=int(date[2])<=31:
            return True
        else:
            return False
        

if Date.is_date_valid('2000-10-31'): #True
    print("올바른 날짜 형식입니다")
else: 
    print("잘못된 날짜 형식입니다")'''

#심화문제(와..나 겁내 더럽게했다)
class Time():

    @classmethod
    def is_time_valid(*cls): #문자열이 올바른지 확인함
        if int(cls[1][0])<=24 and int(cls[1][1])<=59 and int(cls[1][2])<=60:
            print(cls[1][0], cls[1][1], cls[1][2])
        else:
            print("잘못된 입력입니다")

date=input("시:분:초 형식으로 시간을 입력 : ").split(":")
Time.is_time_valid(date)







