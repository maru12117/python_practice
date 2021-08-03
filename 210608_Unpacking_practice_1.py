'''x= map(int,input().split())
print(type(x))
a,b = x
print(a,b)
print(a+b)'''

'''a=list(range(5,-10,-2))
print(a)'''

'''x = int(input("숫자를 입력해주세요"))
list_range=list(range(-10,11,x))
print(list_range)'''

x,y,z = map(int,input("시작하는 값과 끝나는 값, 증가폭의 입력값을 차례때로 입력해주세요 : ").split())
tuple_range=tuple(range(x,y+1,z))
print(tuple_range)


