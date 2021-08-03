'''x = 5
if x != 10:
    print('Ok')'''

'''price = input("가격을 입력해주세요 : ")
coupon = input("쿠폰을  입력해주세요 : ")

if coupon == 'Cash3000':
    print("쿠폰 할인으로 인해", int(price)-3000,"원 입니다")

if coupon == 'Cash5000':
    print("쿠폰 할인으로 인해", int(price)-5000,"원 입니다")'''

'''print(bool(0))
if bool(0) :
    print("참")
else :
    print("거짓")'''


'''written_test = 75
coding_test = True

if written_test >=80 and coding_test==True:
    print("합격")
else :
    print("불합격")'''

korean, english, mathemathic, science = map(int,
                                            input("과목의 점수를 입력하세요 : ").split())
total=korean+english+mathemathic+science
avg = total/4
if 0<=korean<=100 and 0<=english<=100 and 0<=mathemathic<=100 and 0<=science<=100:
    if avg >= 80:
        print("합격입니다")
    else :
        print("불합격입니다")
else:
    print("잘못 된 입력값입니다")


    
    
    
