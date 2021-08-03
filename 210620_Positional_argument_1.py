'''def print_number(a,b,c):
    print(a)
    print(b)
    print(c)
    
x=[10,20,30]
print_number(*x)'''
#가변인수만들기.(넣어주는 값에 따라 다양하게 달라지는 인수)
'''def print_numbers(*args): #매개변수 앞에 *을 붙여서...넣은 숫자 개수만큼 출력됨
    for arg in args:
        print(arg)

print_numbers(10,20,30,40)'''

'''def personal_info(name, age, address):
    print("이름 : ", name)
    print("나이 : ",age)
    print("주소 : ",address)

personal_info('홍길동',30,'서울특별시')'''

'''def personal_info(name, age, address):
    print("이름 : ", name)
    print("나이 : ",age)
    print("주소 : ",address)

personal_info(name='홍길동',age=36,address='서울특별시')'''

'''def personal_info(name, age, address):
    print("이름 : ", name)
    print("나이 : ",age)
    print("주소 : ",address)'''

'''def personal_info(**kwarages):
    for key, value in kwarages.items():
        print(key,": ",value,sep="", end=", ")

x ={'name':'홍길동','age':36,'address':'서울특별시'}
#personal_info(name='홍길동',age=36) #**애스터리스트 2개를 사용함으로써, Dictionary를 unpacking함
personal_info(**x)'''

'''def personal_info(*args): #값은 하나 받는데...주는건 3개
    print(args)

personal_info(*[10,20,30])'''

'''def personal_info(name, age): #고정변수
    print(name, age)

personal_info(**{'name':'홍길동','age':36})'''

#연습문제(가장 높은 점수를 출력하는 함수 만들기)

'''korean, english, mathematics, science=100,86,81,91

def get_max_score(*agrs): #인수가 여러개라서..*한개 써서 활용함
    max_score1=max(agrs)
    return max_score1


max_score=get_max_score(korean, english, mathematics, science)
print('높은 점수', max_score)

max_score=get_max_score(english, science)
print('높은 점수', max_score)'''

#심사문제(가장 높은 점수, 가장 낮은 점수, 평균 점수)

korean, english, mathematics, science=map(int,input("국어, 영어, 수학, 과학 점수를 입력해주세요 : ").split())
def make_score(*sgr):
    return max(sgr), min(sgr), sum(sgr)/len(sgr)

max_score, min_score, avg_score =make_score(korean, english, mathematics, science)
print("가장 낮은 점수는 %.2f, 가장 높은 점수는 %.2f, 평균점수는 %.2f 입니다" % (min_score, max_score, avg_score))





