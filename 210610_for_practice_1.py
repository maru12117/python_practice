'''for i in range(5,12):
    print('Hello world', i)'''

'''for i in range(10,0,-1):
    print('Hello world', i)'''

'''start_num=int(input("시작값을 입력하세요 : "))
end_num=int(input("끝값을 입력하세요 : "))
interval = int(input("간격을 입력하세요 : "))
if interval>0 and start_num<end_num:
    for i in range(start_num,end_num+1,interval):
        print(i)
elif interval<-1 and start_num>end_num:
    for i in range(start_num,end_num-1,interval):
        print(i)
else :
    print("잘못된 입력값입니다")'''


'''a = [10,20,30,40,50,60]
for i in a:
    print(i)'''

'''fruits = ('apple','orange','grape')
for fruit in fruits:
    print(fruit)'''

'''for i in reversed('Python'):
    print(i, end="")'''

'''x = [49,-17,25,102,8,62,21]
for i in x:
    print(i*10, end=" ")'''

'''num=int(input("구구단의 숫자를 입력하세요 : "))
for x in range(1,10):
    print(num,"*",x,"=",num*x)'''

num=int(input("숫자를 입력하세요 : "))
total = 0
for x in range(num+1):
    total = total+x
print(total)



