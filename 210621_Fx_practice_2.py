#계산맞추기 게임 프로젝트

#eval("3+5")
import random

def make_question():
    num1=str(random.randint(-99,99))
    num2=str(random.randint(-99,99))
    cal=random.randint(1,3)
    if cal==1:
        nData=num1+" + "+num2
        return nData
    elif cal==2:
        nData=num1+" - "+num2
        return nData
    elif cal==3:
        nData=num1+" * "+num2
        return nData
    
count=0
ex = 0 #맞춘 개수
while True:
    if count<5:
        ndata=make_question()
        print(ndata)
        dap=int(input("답을 입력해주세요 : "))
        count+=1
        dap1=eval(ndata)
        if dap==dap1:
            print("정답입니다!")
            ex+=1
        else:
            print("오답입니다")
    elif count==5:
        print("총 5문제 중 %d문제 맞췄습니다" % ex)
        break
