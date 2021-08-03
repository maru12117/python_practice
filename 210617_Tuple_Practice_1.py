#처음 찾은 인덱스를 구함
#a= (38,21,53,62,19,53)
'''print(a.index(53))
print(a.count(53))'''

'''for i in a:
    print(i, end=" ")
print()

i = 0
while i<len(a):
    print(a[i], end=" ")
    i += 1
print()
b = tuple(i for i in range(10) if i%2==0)
print(b)

print()'''
#괄호 안에 표현식을 넣으면 튜플이 아니라, 제너레이터로 표시된다

'''c = (1.2, 2.5, 3.7, 4.6)
print(tuple(map(int,c)))

print(min(a))
print(max(a))
print(sum(a))'''

'''a = ['alpha', 'bravo', 'charlie', 'delta', 'echo','foxtrot', 'golf', 'hotel', 'india']
b = [x for x in a if len(x)==5]
#print(b)

#print(len('alpha')) #문자열도 len()함수를 통해서 개수 확인이 가능함
while True:
    num1, num2 = map(int,input("정수를 입력하세요 : ").split())
    if 1<=num1<=20 and 10<=num2<=30:
        break
    else:
        print("다시 입력해주세요")
    
My_list=[2**x for x in range(num1, num2+1)] #리스트 표현식을 사용
My_list.pop(1)
My_list.pop(-2)
print(My_list)'''

#딕셔너리 심화문제
'''ai_classes = {
     'class01' : [
                {'name' : '서준', 'age' : 24},
                {'name' : '하준', 'age' : 34},
                {'name' : '도윤', 'age' : 37},
                {'name' : '시윤', 'age' : 19},
                {'name' : '은우', 'age' : 31}
     ],
     'class02' : [
                  {'name' : '지호', 'age' : 34},
                  {'name' : '예준', 'age' : 19},
                  {'name' : '동원', 'age' : 21},
                  {'name' : '민정', 'age' : 22},
                  {'name' : '효주', 'age' : 24}
     ]
 }

for x in ai_classes:
    print(x)
    print()
    for y in ai_classes[x]: #리스트 타입
        print(y)
        if y["age"]>=30:
            print(y["name"],":", y["age"], end=" \t")
print()

for age in ai_classes: #[i]가 리스트의 크기
    for i in range(len(ai_classes[age])):
        if ai_classes[age][i]['age']>=30:
            print(ai_classes[age][i]['name'],": ", ai_classes[age][i]['age'], end="\t")
print()
print(ai_classes["class01"][0])'''

#연습문제
import random
bin_List=[]
i=0
while i<7:
    num = random.choice(range(1,51))
    if num not in bin_List:
        bin_List.append(num)
        i +=1
bin_List.sort()    
print(bin_List)












