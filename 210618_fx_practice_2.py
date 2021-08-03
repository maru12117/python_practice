#text 계산기만들기

while True:
    def text(first, second,yeosan):
        if yeosan==1:
            result=first+second
        elif yeosan==2:
            result=first-second
        elif yeosan==3:
            result=first*second
        elif yeosan==4:
            result=first/second
        elif yeosan==5:
            result=first%second
        return result
  
    print("=============================================")
    print("1.더하기 \n2.빼기 \n3.곱하기 \n4.나누기 \n5.나머지구하기 \n6.나가기")
    print("=============================================")
    yeosan=int(input("원하는 연산자를 입력하세요 : "))
    if yeosan<=5:
        first=int(input("첫번째 숫자를 입력하세요: "))
        second=int(input("두번째 숫자를 입력하세요: "))
        if yeosan==1:
            result=text(first,second,yeosan)
            print("결과는 %d 입니다 ." % result)
        elif yeosan==2:
            result=text(first,second,yeosan)
            print("결과는 %d 입니다 ." % result)
        elif yeosan==3:
            result=text(first,second,yeosan)
            print("결과는 %d 입니다 ." % result)
        elif yeosan==4:
            if second ==0:
                print("0으로 나눌 수는 없습니다. 다시 입력해주세요 ")
                continue
            result=text(first,second,yeosan)
            print("결과는 %d 입니다 ." % result)
        elif yeosan==5:
            result=text(first,second,yeosan)
            print("결과는 %d 입니다 ." % result)
    elif yeosan ==6:
        print("프로그램을 종료합니다")
        break
    else:
        print("잘못입력하셨습니다")
    
    
