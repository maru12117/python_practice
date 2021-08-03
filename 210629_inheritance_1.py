#상속받기

'''class Person():
    def greeting():
        print("안녕하세요")

class Student(Person): #상속을 받음
    def study():
        print("공부하기")

jame = Person() 
jame.study() #Person은 상속을 안받았기 때문에 study()를 사용못함
jame.greeting()'''

#동등한 관계의 상속(is a-)
'''class Person():
    def greeting(self,day):
        print(day)
        print("안녕하세요")

class Student(Person): #상속을 받음
    def study(self):
        print("공부하기")

jame = Student()
jame.study()
jame.greeting(1)'''

#포함관계의 상속(has a -)
'''class Person():
    def greeting(self):
        print("안녕하세요")

class PersonList:
    def __init__(self):
        self.person_list=[] #빈 리스트를 만듦

    def append_person(self, person):
        self.person.append(person) #속성으로 넣음
        print(self.person_list)

james=PersonList()
maria=PersonList()

james.append_person()'''

#기반 클래스의 속성
'''class Person():
    def __init__(self):
        print("Person __init__") #출력 불가
        self.hello = "안녕하세요" #출력 불가(기반 클래스이 속성을 사용할 수 없음)

class Student(Person):
    def __init__(self):
        print("Student __init__") #출력
        self.school = "파이썬 코딩 도장" #출력

james = Student()
print(james.school)
print(james.hello)'''

#기반 클래스의 속성 사용하기
'''class Person():
    def __init__(self):
        print("Person __init__") #출력
        self.hello = "안녕하세요"  #출력

class Student(Person): #슈퍼클래스의 상속을 받음
    def __init__(self):
        print("Student __init__") #출력
        super().__init__()            #super()을 통해 슈퍼클래스의 __init__메서드 호출
        self.school = "파이썬 코딩 도장" #출력

james = Student()
print(james.school)
print(james.hello)'''

#기반 클래스의 속성을 가져오지 않고 출력하기

'''class Person():
    def __init__(self):
        print("Person __init__") #출력
        self.hello = "안녕하세요"  #출력

class Student(Person): 
    pass  #파생 클래스에서 __init__()메서드가 없다면, 기반 클래스의 속성을 가져오지 안아도 바로 사용이 가능함

james = Student()
print(james.hello)'''

#오버라이딩(Overriding) 사용하기
'''class Person:
    def greeting(self):
        print("안녕하세요") #출력되지 않음

class Student(Person):
    def greeting(self):
        print("코딩 도장입니다.") #출력(슈퍼클래스를 무시함)

james=Student()
james.greeting()'''

#슈퍼클래스를 무시하지않고 중복을 최소화하기 위해서 super().메소드를 활용함
'''class Person:
    def greeting(self):
        print("안녕하세요") #출력

class Student(Person):
    def greeting(self):
        super().greeting() # 기반 클래스에 먼저 들어가서 출력함
        print("코딩 도장입니다.") #출력

james=Student()
james.greeting()'''

#다중 상속사용하기(기반 클래스 2개 , 파생 클래스 1개)
'''class Person:
    def greeting(self):
        print("hi")

class University:
    def manage_credit(self):
        print("manager")

class Undergraduate(Person, University): #2개의 기반 클래스 상속!
    def study(self):
        print("study")

#메서드 탐색 순서 확인하기 mro() : method resolution order
print(Undergraduate.mro())'''

#다이아몬드 상속
class A:
    def print(self):
        print("a")

class B(A): #A를 상속받음
    pass

class C(A): #A를 상속
    pass

class D(B,C): #b와 c를 상속받음
    pass

james=D()
james.print()

print(D.mro())


        










