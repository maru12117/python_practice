'''x = int(input("숫자를 입력해주세요 : "))
if 11<x<20:
    print("11~20")
elif 21<x<30:
    print("21~30")
else:
    print("아무것도 해당되지 않음")'''

age = int(input("나이를 입력해주세요 : "))
x = 9000
if age>=7:
    if 7<=age<=12:
        print("잔액은 ",x-650,"입니다")
    elif 13<=age<=18:
        print("잔액은 ",x-1050,"입니다")
    elif 19<=age:
        print("잔액은 ",x-1250,"입니다")
else :
    print("7세 이하는 요금을 내지 않습니다")
