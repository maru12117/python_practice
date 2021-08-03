# 값 in 시퀀스 객체
'''a = [0,10,20,30,40,50,60,70,80,90]
print(100 in a)'''

#값 not in 시퀀스 객체의 특정 값이 없는지 확인함
'''a = [0,10,20,30,40,50,60,70,80,90]
print(100 not in a)
print(30 not in a)'''

'''print(43 not in (38,76,43,62,19))
print(1 not in range(10))
print('P' not in 'Hello, Python')'''

'''x = int(input("숫자를 입력해주세요 :"))
list_add=list(range(1,20,2))
print(list_add)
print(x in list_add)'''

'''a = [1,2,3]
b = (4,5)
print(a+list(b))'''


'''a = [1,2]
b = [3,4]
c=a+b
print(a+b)
print(a)
print(b)
print(c)'''

a=["사과", "배", "귤","오렌지"]
b = ["토마토","바나나","수박","딸기"]
c=a+b
print("사과" in c)
#논리 연산자를 확인하여 '사과'가 있는지 확인함
print("사과" in a or "사과" in  b)


