'''hour, minute, second = map(int,input("시간을 입력하세요 : ").split(':'))
print("시 :",hour)
print("분 :", minute)
print("초 :",second)'''

'''a,b = input("두개의 숫자를 입력해주세요 :").split()
a = int(a)
b = int(b)
print("두개의 숫자의 합은 ", a+b, "입니다")'''

'''print('python isn\'t difficult')'''

'''i1,i2,i3,i4,i5 = map(int,input("5개의 값을 입력하시오 : ").split())
print("합은", i1+i2+i3+i4+i5)'''

'''korean, english, math, science = map(int,input("국어, 영어, 수학 , 과학 점수를 \
순서대로 입력해주세요 : ").split())
print("4개 과목의 평균점수는 ", int((korean+english+math+science)/4),"입니다")'''

'''print(1,2,3, sep=", ")
print(4,5,6, sep=",")
print('Hello', 'Python', sep='')
print(1920, 1080, sep='x')

print(1,2,3, sep="\n")'''

'''korean, english, math, science = map(int,input("국어 영어 수학 과학 점수를 \
순서대로 입력해주세요 : ").split())
total = korean+ english+ math+ science
print(korean, english, math, science, sep="+")
print("총합은",total, "입니다")'''

'''print(1,end="/")
print(2, end="/")
print(3)'''

'''year= 2019
month = 1
day = 31
hour = 10
minute = 33
second = 57
print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")'''

applePrice = 150
orangePrice = 30
apple, orange = map(int,input("사과와 귤의 수를 '/'로 나누어서 차례대로 입력해주세요 : ").split("/"))
total = applePrice*apple+orangePrice*orange
print()
print("총 가격은", total, "원")


