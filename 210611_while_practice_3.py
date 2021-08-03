import random
#random.random()은 0<= random.random()<=1 이기때문에
#random.randint를 사용하여 범위를 정한
'''i=0
while i<10:
    print(random.randint(1,9))
    i+=1'''

'''import random

cnt_rand = [0,0,0,0,0,0]
i=0
while i<10:
    num = random.randint(1,6)
    print(num)
    cnt_rand[num-1] = cnt_rand[num-1] + 1
    i +=1
print(cnt_rand)'''


'''num = 0
while num !=3:
    num = random.randint(1,6)
    print(num)'''

userNum = 0
num = random.randint(1,30)
while num != userNum:
    userNum = int(input("숫자를 맞혀보세요 : "))
    if userNum < num:
        print("너무 작습니다")
    elif userNum > num:
        print("너무 큽니다")
    else :
        print("정답입니다")
print("게임을 종료합니다")





