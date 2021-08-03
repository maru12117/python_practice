'''num = int(input("반복하고자 하는 숫자를 입력해주세요 : "))
i = 0
while i<num:
    print('Hello world', num)
    num -= 1'''


'''count = int(input("반복할 횟수를 입력하세요 : "))

while count>0:
    print("Hello world", count)
    count -= 1'''
'''i=1
while i<=10:
    print(i, end="  ")
    i += 1

for x in range(1,11):
    print(x, end="  ")'''

'''i = -50
count=1
while i<=1:
    if count%3 == 0:
        print(i, count, end="\t")
        print() #줄 바꿈 표시
    else:
        print(i, count, end = "\t")
    i += 1
    count +=1'''

'''num= int(input("정수를 입력해주세요 : "))
i=1
total=0
while i<=num:
    total=total+i
    i += 1
print(total)'''

'''num= int(input("정수를 입력해주세요 : "))
i =1
while i<10:
    print(num,"X", i, "=",num*i, sep=" ")
    i+=1'''

mark = list(map(int,input("점수를 입력해주세요 : ").split()))
i=1
num=len(mark)
print(mark)
while num>0:
    if mark[i-1]>=60:
        print(i,"번 학생은 합격입니다")
    else:
        print(i,"번 학생은 불합격입니다")
    i += 1
    num -= 1

'''marks=[90, 25, 67, 45, 80]
i = 0
while i<5:
    if marks[i] >= 60:
        print(i,"번 학생 축하합니다 합격입니다")
    else:
        print(i,"번 학생 불합격입니다")
    i +=1'''

'''Kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
i = 0
total = 0
while i<10:
    total = total+Kor[i]
    avg = total/len(Kor)
    i += 1
print(avg)'''



