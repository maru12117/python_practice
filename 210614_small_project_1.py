#1
'''for x in range(1,11):
    print(x, end=" ")
print()
i = 1
while i<=10:
    print(i, end=" ")
    i += 1'''

#2
'''start, end=map(int,input("두개의 정수를 입력하세요 : ").split())
total = 0
for i in range(start, end+1):
    total = total + i
print(total)


total=0
while start<=end:
    total = total+start
    start += 1
print(total)'''

#3
'''start, end=map(int,input("두개의 정수를 입력하세요 : ").split())
total=0
for x in range(start, end+1):
    if x%2==0:
        y = x**2
        total = total+ y
print(total)

total=0
while start<=end:
    if start%2==0:
        y=start**2
        total=total + y
    start = start+ 1
print(total)'''

#4
'''Kor = [70,60,55,75,95,90,80,80,85,100]
total=0
for x in Kor:
    total += x
    avg = total/len(Kor)
print(avg)

Kor = [70,60,55,75,95,90,80,80,85,100]
total=0
x = 0
while x<len(Kor):
    total += int(Kor[x])
    x += 1
avg = total/len(Kor)
print(avg)'''

#5
'''total=0
for x in range(1,1000):
    if x%3==0 or x%5==0:
        total = total+x
print(total)
x=0
while x<1000:
    if x%3==0 or x%5==0:
        total = total+x
    x += 1
print(total)'''

#6
'''grade = list(map(int,input("실기점수를 입력하세요 : ").split()))
total=0
for x in grade:
    total = total + x
    
max = 0
for y in grade:
    if y > max:
        max = y
print("최대 : ", max)
        
min = 100
for z in grade:
    if z < min:
        min = z
print("최소 : ", min)
total = total -(max+min)
avg = total/(len(grade)-2)
print(avg)'''

#7
grade_counter=[0,0,0,0,0]
score = list(map(int,input("점수를 입력하세요 : ").split()))

for x in score:
    if 85<=x<=100:
        grade_counter[0] += 1
    elif 70<=x<=84:
        grade_counter[1] += 1
    elif 55<=x<=69:
        grade_counter[2] += 1
    elif 40<=x<=54:
        grade_counter[3] += 1
    elif 0<=x<=39:
        grade_counter[4] += 1
print(grade_counter)



















    
    
