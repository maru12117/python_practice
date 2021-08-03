'''i = 2
j = 5

while i<34 or j>1:
    print(i, j, sep=" ")
    i *= 2
    j -= 1'''

'''money = int(input("금액을 충전합니다 : "))

while money >= 1350:
    money = money - 1350
    print(money)'''

#3으로 끝나는 숫자만 출력하기(10으로 나눈 나머지가 3)
'''i = 0
while True:
    if i%10!=3:
        i +=1
        continue
    if i >74:
        break
    print(i, end= " ")
    i +=1'''


a, b = map(int,input("두개의 정수를 입력해주세요 : ").split())
while True:
    if a%10==3:
        a +=1
        continue
    if a >= b+1:
        break
    print(a, end= " ")
    a +=1
