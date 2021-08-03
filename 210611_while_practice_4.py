'''while 'Hello world':
    print("Hello world")'''

'''i = 2
j = 5

while i<=32 or j>0 :
    print(i, j)
    i *= 2
    j -=1'''

'''i = 0
total = 0
while True:
    total = total + i
    i += 1
    if i ==100:
        break
print(total)'''

'''total = 0
for i in range(10000):
    total = total + i
    if i == 100:
        break
print(total)'''

'''for i in range(100):
    if i % 2==0:
        continue #생략의 의미
    print(i)'''
'''i =0
while i < 100:
    i += 1
    if i %2 ==0:
        continue
    print(i)'''

'''count = int(input("반복횟수 입력 : "))

for i in range(10000):
    print(i)
    if i == count:
        break'''

'''i = 0
while True:
    if i%10!=3:
        i+=1
        continue
    if i>73:
        break
    print(i, end=" ")
    i+=1'''

start, stop = map(int,input("정수 두개를 입력하세요 : ").split())
i = start
while True:
    if i%10==3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=" ")
    i+=1
    

