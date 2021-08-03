
menu=["사이다","콜라","생수","쥬스","커피"]
price=(1200,1100,700,1500,1300)
money=(10000,5000,1000,500,100)
total_price=0

while True : ##금액 투입
    print("================================================================")
    print("1번 10,000원, 2번 5,000원, 3번 1,000원 \n4번 500원, 5번 100원, 0번 입력완료(99번 재고관리 프로그램)")
    button_price=int(input("투입 금액을 입력해주세요 : "))
    if button_price == 1 or button_price == 2 or button_price == 3 or button_price == 4 or button_price == 5:
        total_price += money[button_price-1]
    elif button_price == 0 or button_price == 99:
        break
    else:
        print("다시 입력해주세요 ")
        print()
    print("투입금액은 : ", total_price, "입니다.\n")
print("총 투입금액은 : ", total_price, "입니다.\n")
stock=dict(zip(menu, [3,3,3,3,3]))
print()

while button_price == 99: ##재고관리 프로그램
    print("================재고관리 프로그램 입니다 =======================")
    button_stock = int(input("1: 추가, 2:제거, 3: 현재수량확인 (0번 나가기) "))
    if button_stock ==1 :
        stockchoice = int(input("[재고추가] 제품을 선택하세요 1.사이다 2.콜라 3.생수 4.쥬스 5. 커피 : "))
        if stockchoice == 1 or stockchoice == 2 or stockchoice == 3 or stockchoice == 4 or stockchoice == 5:
            print(menu[stockchoice-1], "는 ", stock[menu[stockchoice-1]],"의 재고가 있습니다.")
            stock_plus=int(input("[재고 추가] 몇개를 추가하나요? : "))
            stock[menu[stockchoice-1]]+=stock_plus
            print(menu[stockchoice-1],"의 수량이" , stock[menu[stockchoice-1]],"개 로 변경되었습니다.")
        else:
            print("다시입력해주세요 ")
            continue
    elif button_stock ==2:
        stockchoice = int(input("[재고 삭제] 제품을 선택하세요 1.사이다 2.콜라 3.생수 4.쥬스 5. 커피 : "))
        if stockchoice == 1 or stockchoice == 2 or stockchoice == 3 or stockchoice == 4 or stockchoice == 5:
            print(menu[stockchoice-1], "는 ", stock[menu[stockchoice-1]],"의 재고가 있습니다.")
            stock_plus=int(input("[재고 삭제] 몇개를 제거하나요? : "))
            stock[menu[stockchoice-1]]-=stock_plus
            print(menu[stockchoice-1],"의 수량이" , stock[menu[stockchoice-1]],"개 로 변경되었습니다.")
    elif button_stock ==3:
        print("[현재 재고량]", stock)
    elif button_stock ==0:
        break
    else:
        print("다시 입력해주세요")
        
while total_price >0 : ## 물건 구매
    print("===========================자판기 메뉴==========================")
    for x in range(5):
        print(x+1,"번", menu[x]," : ",price[x], "원")
    print("================================================================")
    button_menu = int(input("원하시는 음료를 선택해주세요 (0번은 완료): "))
    if button_menu==1 or button_menu==2 or button_menu==3 or button_menu==4 or button_menu==5:
        if stock[menu[button_menu-1]] <= 0: #재고량이 적을 시 다시 선택
            print("※ 재고가 부족합니다 ※")
            print("[현재 재고]", stock)
            print()
            continue
        
        if total_price > price[button_menu-1] : #투입금액이 물품금액보다 클때만 결제
            total_price -= price[button_menu-1]
            stock[menu[button_menu-1]]-= 1
            print(menu[button_menu-1],"메뉴를  선택하셨습니다. \n[남은 잔액] ",total_price,"입니다. ")
        elif total_price < price[button_menu-1]:
            print("※ 잔돈이 부족합니다 ※")
            break
        
    elif button_menu==0:
        break
    else:
        print("다시 입력해주세요 ")
        continue
print()        
print("[남은 잔액]", total_price,"을 반환합니다")
print()
balance_list=[0,0,0,0,0] #반환금액을 리스트에 넣음

if total_price>0 : #반환금액 최소한의 단위로 나누기
    while total_price>=10000:
        balance_list[0] +=1
        total_price -= 10000
    while total_price>=5000:
        balance_list[1] +=1
        total_price -= 5000
    while total_price>=1000:
        balance_list[2] +=1
        total_price -= 1000
    while total_price>=500:
        balance_list[3] +=1
        total_price -= 500
    while total_price>=100:
        balance_list[4] +=1
        total_price -= 100

    print("10,000원 지폐", balance_list[0],"장\t", "5,000원 지폐", balance_list[1],"장\n","1,000원 지폐", balance_list[2],"장\t",
      "500원 동전", balance_list[3],"개\n", "100원 동전", balance_list[4],"개를 잔돈으로 반환합니다")

print("다음에 또 이용해주세요!")
    

        



















        
        
        

