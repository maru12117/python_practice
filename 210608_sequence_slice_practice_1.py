# 시퀀스 슬라이스 : 시퀀스 객체의 일부를 잘라냄
# 시퀀스 객체[시작 인덱스 : 끝인덱스의 앞에 인덱스까지 자름(해당 인덱스는 포함안됨)]
a = [0,10,20,30,40,50,60,70,80,90]
'''print(a[0:4])'''

#a[1:1]로 하면 값이 없음
'''print(a[1:1])
print(a[1:2])
print(a[4:7])
print(a[4:-1])'''

# 인덱스 두번쨰꺼 부터 시작해서 8번쨰(포함하지않음) 전까지 해서 3의 증가폭을 가짐
'''print(a[2:8:3])'''

#슬라이스를 사용할 때 시작인덱스와 끝 인덱스를 생략할 수도 있음
'''print(a[7:])'''

#시작과 끝인덱스를 둘다 생략하면, 리스트 전체가 출력됨
'''print(a[:])
print(a[:7:2])
print(a[7:len(a):2])
print(a[len(a)-1])

print(a[::2])'''

'''print(a[:len(a)])'''

b = (0,10,20,30,40,50,60,70,80,90)

'''print(b[4:7])
print(b[4:])
print(b[:7:2])'''

r = range(10)
'''print(list(r))
print(list(range(4,7)))
print(r[4:7])
print(r[4:])
print(r[:7:2])'''

hello = 'Hello, world!'
'''print(hello[2:9])'''

#슬라이스로 요소 할당하기(원래있떤 리스트가 변경되며, 새 리스트는 생성되지 않음)
a = [0,10,20,30,40,50,60,70,80,90]
a[2:5] = ['a','b','c']
print(a)



