#a리스트에서 값이 30인 인덱스를 구하시오
'''a = [11,12,30,56,65,25,89,30,56,32,30,65,98,30,65,56,30,56,98,30]
bin_List= [ ] #인덱스 집어넣을 리스트를 생성함
for x in range(len(a)-1):
    if a[x]==30:
        print(x, end=" ")

while True:
    val=a.index(30)
    print(val)
    bin_List.append(val)
    a[val]="x"
    if 30 not in a:
        break

print(a)
print(bin_List)'''

#줄바꾸기 7줄마다...(줄바꾸기)
#1~100까지의 정수 중에서 짝수를 나열(while문 사용)하는데, 5줄로 연결하기
i=1
count=0
while i<=101:
    if i%2==0:
        print(i, end="\t")
        count +=1
        if count%5==0:
            print()
            count==1
    i+=1


