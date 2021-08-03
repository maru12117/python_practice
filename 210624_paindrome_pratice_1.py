#회문은 거꾸로 읽어도 제대로 읽은것과 같은 단어와 문장을 말함
word="level"
#print(word[0:1]) #l
'''print(len(word))
i=1
while i-1<len(word)//2:
    if word[i-1]==word[-i]:
        print("회귀")
    else:
        print("회귀 아님")
    i+=1'''

#반복문으로 문자 검사하기
'''word=input("단어를 입력하세요 : ")
in_palindrome = True #회문값 판별값을 저장할 변수
for i in range(len(word)//2): #0부터 문자열 길이의 반만큼만 반복함
    if word[i]!=word[-1-i]: #0이랑 -1이 비교됨 아!처음부터 틀리면 끝.! 바로 회문 값아님.
        in_palindrome=False
        break
print(in_palindrome)'''

#시퀀스 객체 비교
'''word=input("단어를 입력하세요 : ")
if word == word[::-1]: #반대로
    in_palindrome = True
else:
    in_palindrome = False
print(in_palindrome)'''

#reversed 사용
'''word=input("단어를 입력하세요 : ")

if list(word) == list(reversed(word)): 
    in_palindrome = True
else:
    in_palindrome = False
print(in_palindrome)'''

#N-gram만들기(반복문으로 만들기)
'''word="this is python script"
text=word.split(" ")

for i in range(len(text)-1):
    print(text[i], text[i+1], sep=" ")'''

#zip으로 N-gram 만들기
'''text = 'hello'
word=zip(text, text[1:]) #튜플 형태로 묶어줌 ('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')
for i in word:
    print(i[0], i[1], sep="") #튜플에서 0번째랑 1번쨰인덱스의 값을 가져옴'''

'''text="this is python script"
text_list=text.split(" ")
word=list(zip(text_list, text_list[1:]))
for x in word:
    print(x[0], x[1], sep=" ")'''

#리스트 표현식
'''text = "hello"
text_list=[text[i:] for i in range(3)]
print(list(zip(*text_list))) #콤마로 구분해서 넣어주기

print(list(zip(*[text[i:] for i in range(4)])))'''

#연습문제

'''n = int(input("정수를 입력하세요(N-gram표현) : "))
text=input("문자열을 입력해주세요 : ").split(" ")
if n<len(text):
    list_text=list(zip(*[text[i:] for i in range(n)])) #튜플로 출력함
    for x in range(len(list_text)):
        print(list_text[x])
else:
    print("wrong")'''

#심사문제

with open("word.txt","r",encoding="utf-8") as file:
    while True:
        word=file.readline()
        if word=="":
            break
        word1=word.replace("\n","")
        if word1==word1[::-1]: #시컨스 뒤집기...word1[::-1]
        #if list(word1)==list(reversed(word1)): #reversed를 먼저 문자열에 사용하고, 리스트하기
            print(word1)




    
    
    
