'''a = {"헝가리":[1,2], "아지르":[2,3],"시비르":[4,5]}

def research_total(**a):
    for x,y in a.items():
        print(x,y)
        return x,y
    
    
research=research_total(**a)
print(research)'''


#for 반복문으로 두번사용하여 각각 출력하기
#a = [[10,20],[30,40],[50,60]]

'''for x in a:
    for y in x:
        print(y, end=" ")
    print()'''

#range를 사용하여 a출력하기
'''for x in a: #[10,20]
    for y in range(len(x)): #0,1
        print(x[y], end=" ")
    print()'''

#while 문을 사용하여 a 출력하기
'''i=0
while i<len(a): #0,1,2
    j=0
    while j<len(a[i]): #0,1
        print(a[i][j], end=" ")
        j+=1
    print()
    i+=1'''
#리스트 표현식
#a = [[0 for x in range(2)] for y in range(3)]
#a = [[0]*2 for y in range(3)]
'''b=[3,1,3,2,5]
a =[[[0]*i] for i in b]
print(a)'''

#a = [[[0 for i in range(3)]for y in range(4)]for z in range(2)]
#print(a)

#파일명만 가져오기
path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-32\\data.txt'
filename=path.split("\\") #\\대로 분리함
print(filename[-1])


#특정 단어만 가져오기
b = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
b1=b.replace(","," ").replace("."," ").count("the ")#, 및 .을 모두 없앰
print(b1)



