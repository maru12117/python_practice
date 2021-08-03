num = int(input("임의 숫자를 입력하세요 : "))
binList = [0]*1000
currQuot = num #입력받은 숫자를 몫으로 표현
digitCnt = 0 #2진수 자리의 개수를 0으로 표현

while currQuot >0: #일단 입력받은 수가 0보다 크기때문에 해당 while문 투입
   binList[digitCnt]= int(currQuot % 2) #입력받은 수를 2로 나눈 나머지를 빈리스트에 넣음
   #넣으면....아마 [10000000] 이 출력됨
   currQuot = int(currQuot/2) #2로 나눈 몫을 구하기 위해 정수타입으로 출력
   digitCnt +=1 #다시 루프가 실행되면, 다음 나머지를 binList의 다음 인덱스로 넣기위함임
   
for i in reversed(range(digitCnt)): #binList인덱스의 개수에 따라 for문을 실행
    print(binList[i], end=" ")
   

