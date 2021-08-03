#1
'''name_list=['matthew','mark','luke','john','paul','peter']
count = [0]
for x in name_list:
    if 'h' in x or 'm' in x :
        count[0] += 1
        print(x)
print(count[0])

count=0
for name in name_list:
    for n in name:
        if n=='m' or n=='h':
            count += 1
            print(name)
            break
print(count)'''

#2
'''marks = [90,25,67,45,80]
count=0
for x in marks:
    if x <60:
        print(count, "번 학생 불합격입니다")
        count+=1
        continue
    print(count, "번 학생 축하합니다. 합격입니다")
    count+=1

marks = [90,25,67,45,80]
count=0
while count<len(marks):
    if marks[count]<60:
        print(count+1, "번 학생 불합격입니다")
        count += 1
        continue
    print(count+1, "번 학생 합격입니다. 축하합니다")
    count+=1'''


#3
'''arr = [1,4,2,3]
left, right = 0, len(arr)-1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left +=1
    right -=1
print("변환된 arr은 ", arr, "입니다")'''

#4

'''for x in range(1,10):
    for y in range(2,10):
        print(y,"X",x,"=",y*x,sep=" ", end="\t")
    print()'''
    
'''x=2
y=2
while x<10:
    while y<10:
        print(y,"X",x,"=",y*x, sep=" ", end="\t")
        y +=1
    x +=1
    y = 2
    print()'''

#5
'''vote= [2,5,3,4,1,5,1,5,5,3]
candidates = ["","전정국","김남준","박지민","정호석","김태형"]
vote_list= [0,0,0,0,0,0]
for x in vote:
        vote_list[x] +=1
vote_list = [0, 2, 1, 2, 1, 4]

max =0
i =1
while i < len(vote_list):
    if vote_list[i]>max:
        max = vote_list[i]
        elected = i #후보 인덱스 저장
    i += 1
    
print(candidates[elected],"후보가 총", vote_list[elected],"표를 얻어 당선입니다")'''

#6 광고판 문제
'''num=0
i =0

num=int(input(" : "))
while i < num:
    j = 0
    while j <num:
        print((i+j)%num+1, end=" ")
        j +=1
    print()
    i += 1'''

#7
'''i = 1
total = 0
while i<=100:
    if i%2==0:
        n = i**2
        total = total+n
        i += 1
    else:
        n = i**2
        total = total-n
        i += 1
print(total)'''

#8 소수구하기
num = int(input(" : "))
i = 2

line=0
while i <=num:
    j = 2
    while j<=i: #소수 확인하기
        if i%j ==0:
            break
        j += 1
    if i==j :
        print(i, end="\t")
        line = line+1 #줄 바꾸기
        if line %7==0:
            line = 0
            print()
    i += 1


        
        

        
        
        
    


    










