a = [10,20,30,40,50,20,60]
#a리스트에서 20이라는 값의 개수를 구하기
'''print(a.count(20))'''
# a리스트를 거꾸로 출력함
'''a.reverse()
print(a)'''

#리스트의 요소를 작은 순서대로 정렬함
b=[10,20,56,41,89,12,21,56]
b.sort() # 리스트의 값을 작은 순서대로 정렬함, 오름차순으로 정렬
#print(b)

b.sort(reverse=True) #리스트의 값을 큰 순서대로 정렬함, 내림차순으로 정렬
#print(b)

a= [10,20,30,15,50,20,64]
'''a.sort()
print(a[0]) #최소값
print(a[-1]) #최대값
a.sort(reverse=True)
print(a[0]) #최대값
print(a[-1]) #최소값'''

#모든 요소를 삭제하기
'''a.clear()
print(a)

del a[:] #전체 인덱스
print(a)'''
#가장 끝에서 +1을 추가한 인덱스에 리스트 []로 500을 추가함(append)
'''a[len(a):]=[500,600] 
print(a)'''
#a[len(a):]는 시작 인덱스를 les(a)로 지정해서 가장 끝 인덱스까지 이어가겠다는 뜻임
#a.extend([500,600])과 같은 뜻임
'''a.extend([400,688])
print(a)'''

#리스트 복사하기(하지만 실제로는 리스트는 1개일뿐, 완전히 복사하려면 copy를 써서 객체를 만들어야 함
c=[0,0,0,0,0,0,0]
'''d=c #예를들어 집주소를 공유하는 것임(어차피 같은 객체)
d[2]=4
print(c)
print(d)
print(c is d)''' #c와 d는 같은 객체
#따로 copy()메소드를 활용하여 따로 리스트를 만들어서 생성해야함
'''e=c.copy()
print(c == e) #값은 같음
e[2]=5
print(e)
print(c is e)''' #c와 d는 다른 객체임, 따라서 기존의 리스트를 보관하고 관리하고 싶을때 사용함

d =[38,21,53,62,19]
'''for x in [38,21,53,62,19]:
    print(x)'''
#인덱스와 값이 같이 출력되도록 함 enumerate
'''for index, value in enumerate(d, start=1): #start=1로 지정해주면 인덱스가...알아서 1부터 시작한
    print(index, value)'''

'''e_list=[]
e = [10,20,30,40,20,50,20,30,60,70,20]
for index, value in enumerate(e):
    if value == 20:
        e_list.append(index)
print(e_list)'''
'''f_list_1=[]
e = [10,20,30,40,20,50,20,30,60,70,20]
f = [38,21,53,62,19]
while True:
    f_index=f.index(20)
    f_list_1.append(f_index) #인덱스를 집어넣음 리스트에다가..
    f[f_index] = 'x'
    if 20 not in e:
        break
print(e_list_1)'''

'''e = [10,20,30,40,20,50,20,30,60,70,20]
g = [38,21,53,62,19]
i=0
while i<len(g):
    print(g[i])
    i+=1'''

g = [38,21,53,62,19]
'''max_num=g[0]
mini_num=g[0]
for x in range(len(g)):
    if a[x]>max_num:
        max_num=g[x]
    elif a[x]<mini_num:
        mini_num=g[x]

print(max_num, mini_num)'''

g.sort()
print(g[0])

g.sort(reverse=True)
print(g[0])
    
    













