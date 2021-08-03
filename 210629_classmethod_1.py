'''class Person():
    count =0 #클래스의 속성

    def __init__(self):
        Person.count += 1 #인스턴스가 생성될때마다...Person class의 count가 추가됨

    @classmethod
    def print_count(cls): #클래스 인스턴스를 cls로 받아옴
         print("인스턴스가 총 %s명이 생성되었습니다 " % Person.count)

    @classmethod
    def create(cls):
        p = cls()
        return p #인스턴스 생성

maria=Person()
james=Person() #인스턴스 2개가 생성됨

Person.print_count() #클래스내의 Print_count 함수가 작동
max1=Person.create()
print(max1)'''

#연습문재

class Date():

    @classmethod
    def is_date_valid(cls, hour, minute, second): #클래스에서 받은 것은 2개
        if hour<=24 and minute<= 59 and second<=60:
            return True
        else:
            return False

hour, minute, second=map(int,input("시간을 입력해주세요 : :").split(":"))
if Date.is_date_valid(hour, minute, second): #True
    print("{0} {1} {2}".format(hour, minute, second))
else:
    print("잘못된 날짜 형식입니다") #False







