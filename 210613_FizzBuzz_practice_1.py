'''for x in range(101):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)'''

'''for i in range(101):
    print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)'''

'''for i in range(101):
    if i%2==0 and i%11==0:
        print("FizzBuzz")
    elif i%2==0:
        print("Fizz")
    elif i%11 ==0:
        print("Buzz")
    else:
        print(i)'''
a, b = map(int,input("정수 2개를 입력해주세요 : ").split())
for i in range(a,b+1):
    if i%5==0 and i%7==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Fizz")
    elif i%7 ==0:
        print("Buzz")
    else:
        print(i)
    
