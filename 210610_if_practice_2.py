#1번
'''num = int(input("숫자를 입력해주세요 : "))
if num%2==0:
    print("짝수")
elif num%2!=0:
    print("홀수")'''

#2번
'''num = int(input("숫자를 입력해주세요 : "))
results = num+20
if results<=255:
    print("출력값 :", results)
elif results>255:
    print("출력값 :", 255)'''

#3번
'''num = int(input("숫자를 입력해주세요 : "))
result = num - 20
if result >= 0:
    print("출력값 : ",result)
elif result <0:
    print("출력값 : 0")'''

#4번
'''num = int(input("숫자를 입력해주세요 : "))
result = num -20
if result<0:
    result = 0
elif result>=255:
    result = 255
else:
    result
print("출력값은 :", result)'''

#5
'''time = input("현재시간을 입력해주세요 : ")
print(time)
if time[3:] == '00':
    print("정각입니다")
else:
    print("정각이 아닙니다")'''


#6
'''age = input("나이를 입력해주세요 : ")
age = int(age[0:-1])
print(age,"세")
if 0<= age <19:
    print("청소년입니다")
elif 19<=age<=99:
    print("성인입니다")
else:
    print("잘못된 입력입니다")'''

#7
'''fruits=["사과","포도","홍시"]
fruit = input("좋아하는 과일은 : ")
if fruit in fruits:
    print("정답입니다")
else:
    print("오답입니다")'''

#8
'''warn_investment_list=["Microsoft","Google","Naver","KaKao","LG","SAMSUNG"]
investment_name = input("종목명을 입력해주세요 : ")
if investment_name in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")'''

#9
'''fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
season = input("제가 좋아하는 계절은 : ")
#키값을 확인하기 위해서는 .Keys() and values()
if season in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")'''

'''fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
season = input("제가 좋아하는 과일은 : ")
if season in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")'''

'''money = int(input("금액을 입력해주세요 : "))
if 0<money<= 10000:
    button=int(input("음료를 선택해주세요 1-사이다, 2-콜라, 3-오렌지쥬스 : "))
    if button == 1 and money >= 700:
        balance = money - 700
        print("잔액은 ", balance,"입니다. ")
    elif button ==2 and money >= 600:
        balance = money-600
        print("잔액은 ", balance,"입니다. ")
    elif button == 3 and money >= 800:
        balance = money - 800
        print("잔액은 ", balance,"입니다. ")
    else :
        print("금액이 부족합니다")
else:
    print("금액이 초과되었습니다")'''

#10
'''items = {"사이다":700, "콜라":600,"오렌지쥬스":800}
money = int(input("금액을 입력해주세요 : "))
if money>10000:
    print("최대 금액이 초과되었습니다")
else :
    beverage=input("음료를 선택해주세요 (예시:1. 사이다, 2. 콜라, 3. 오렌지쥬스) : ")
    balance = money - items[beverage]
    if beverage in items and balance>=0 :
        print("잔액은 :", balance)
    else :
        print("잔액이 부족합니다")'''

#11
'''num1 = int(input("첫번째 숫자를 입력해주세요 : "))
num2 = int(input("두번째 숫자를 입력해주세요 : "))
kiho = input("연산자를 입력해주세요 : ")
kihos = ["+","-","*","/"]
if kiho in kihos:
    if kiho == '+':
         print("정답 ", num1+num2)
    elif kiho == '-':
         print("정답 ", num1-num2)
    elif kiho == '*':
         print("정답 ", num1*num2)
    elif kiho == '/':
        if num2 != 0:
            print("정답 ", num1/num2)
        else:
            print("0으로 나누기를 할 수 없습니다")
else:
    print("연산자를 정확하게 입력해주세요 : ")'''

'''num1 = int(input("첫번째 숫자를 입력해주세요 : "))
num2 = int(input("두번째 숫자를 입력해주세요 : "))
kiho = input("연산자를 입력해주세요 : ")
if kiho == "/" and num2==0:
    print("예외")
    
kihos = {"+":num1+num2,"-":num1-num2,"*":num1*num2,"/":num1/num2}
if kiho not in kihos :
    print("연산자가 잘못되었습니다")
else :
    print(kihos[kiho])'''

#12
'''fruit={"apple":150,"orange":30}
apple_num = int(input("사과 개수 : "))
orange_num = int(input("귤 개수 : "))
if apple_num >=5 and orange_num>=3 :
    total_price = (apple_num*fruit["apple"]+orange_num*fruit["orange"])*0.7
    print(total_price)
else:
    print(apple_num*fruit["apple"]+orange_num*fruit["orange"])'''

#13
year = int(input("연도를 입력해주세요 :" ))
if year%4==0:
    if year%100==0:
        print("윤달이 없습니다")
    elif year%400==0:
        print("윤달이 있습니다.")
else :
    print("윤달이 아닙니다.")
    

















        
    
