#재귀함수에 count를 지정하여 무한반복하는 것을 통제함

'''def hello():
    print("hello world")
    hello()

hello()'''


'''def hello(count):
    if count ==0:
        return
    print("hello world", count)
    count -=1
    hello(count) #함수 안쪽의 호출에도 count를 넣어야함

hello(5)'''

'''def factorial(num):
    total=1
    for x in range(1,num+1):
        total*=x
    print(total)


factorial(5)'''

'''def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1) #5*4

print(factorial(4))'''

#재귀호출로 회문 판별하기
'''def is_palindrome(word):
    if len(word)<2: #해당 문자열은 2개 이상이여야 함
        return True
    if word[0]!=word[-1]:
        return False
    print(word)
    return is_palindrome(word[1:-1]) #0부터 시작하지않고, 처음과 끝을 제외하고

#print(is_palindrome('hello'))
print(is_palindrome('level'))'''

#피보나치의 수
num=int(input("1개의 숫자를 입력하세요 : "))
def pibo(num):
    pibo1=0
    if num<1:
        return
    pibo2=(num-1)+num
    pibo1 +=pibo2
    pibo(num-1)
    print(pibo1)
    return pibo1

print(pibo(num))


