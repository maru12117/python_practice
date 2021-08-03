#1.
hour, minute, second = map(int,input("시간을 ':'로 구분하여 입력해주세요 : ").split(":"))
print("시 : ", hour)
print("분 : ", minute)
print("초 : ", second)

#2
korean, english, math, science = map(int, input("국어 영어 수학 과학 순서대로 점수를 입력해주세요 :").split())
total = korean + english + math + science
avg= float(total/4)
print("각 과목의 평균 점수는 ", avg,"입니다")

#3
korean, english, math, science = map(int, input("국어 영어 수학 과학 순서대로 점수를 입력해주세요 :").split())
total = korean + english + math + science
print(korean, english, math, science, sep="+")
print("총합은", total,"입니다")


#4
year = 2019
month = 1
day =31
hour = 10
minute = 33
second=57
print(year, month, day, sep="/")
print(hour, minute, second, sep=":")
