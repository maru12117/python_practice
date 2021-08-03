

'''a[5:]=[62, 72,56,98 ] #리스트로 쭉쭉 이어나감
#len(a)은 제일 끝의 인덱스를 지칭함

print(a)'''
#b=a.copy() #같은 리스트

'''print(a is b)'''

'''c = [12, 35, 65, 89, 63]
for x, y in enumerate(a,1):
    print(x, ": " ,y)'''

'''i=0
while i<len(c):
    print(c[i])
    i+=1'''

c = [51, 35, 26, 89, 63,89,59]
b = [77,98,85,5]
'''smallest = c[0]
for x in c:
    if x < smallest:
        smallest = x
        
print(smallest)'''
'''largest = c[0]
for x in c:
    if x > largest:
        largest=x
print(largest)'''

'''c.sort(reverse=True)
print(c[0])'''
'''i = 0
for x in c:
    i += x'''
'''print(i)

sum(c)'''

'''d = b+c
print(d)
cut=0
for x in d:
    print(x, end="\t")
    cut = cut+1
    if cut%3==0 :
        cut==0
        print()'''

'''a = ['alpha', 'bravo', 'delta', 'hotel', 'india','echo','foxtrot','golf', 'charlie']
b = [i for i in a if len(i)==5]
print(b)'''

'''for x in range(9):
    if len(a[x]) == 5:
        print(a[x])'''

a,b = map(int, input("두개의 정수를 입력하세요 : ").split())
second_list=[]
i=0
for x in range(a,b+1):
    results=2**x
    print(results)
    second_list.append(results)
    i += 1
print(second_list)
del second_list[1]
second_list.pop(-2)
print(second_list)




