'''print('Hello, world'.replace('world','Python'))

s = 'Hello, world'
s=s.replace('world','Python') #변수로 변환시켜주면...변경한 것이 지속적으로 유지됨
print(s)'''

#내가 원하는 문자열의 기준이된
'''table=str.maketrans('aeiou','12345')
print('apple'.translate(table))'''

#split()는 각 문자열을  리스트로 분류한다
'''print('apple pear grape pineapple orange'.split())
print('apple, pear, grape, pineapple, orange'.split(',')) # , 을 기준으로 분류한다'''

#join 리스트 문자열과 구분자 문자열을 연결하는 것(리스트 문자열을 구분자 문자열을 합쳐서 하나의 문자열을 만듦
'''print(' '.join(['apple','pear','grape','pineapple','orange']))
print('-'.join(['apple','pear','grape','pineapple','orange']))'''

#대문자로 바꾸기 upper(), 소문자로 바꾸기 lower()

'''print('Python'.upper())
print('Python'.lower())'''

#왼쪽 공백 삭제하기
'''print('        Python    '.lstrip())
#오른쪽 공백 삭제하기
print('        Python    '.rstrip())
#양쪽 공백 삭제하기
print('        Python    '.strip())'''

#왼쪽의 특정 문자 삭제하기
'''print(' - ,      Python  .  '.lstrip(', .'))
print(' - ,      Python  .  '.rstrip(', .'))'''

#문자열을 정렬하기 칸을 10칸으로 나누어서 왼쪽부터 정렬 ljust& 칸을 10칸으로 나누어서 오른쪽부터 정렬rjust
'''print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10)) #가운데 정렬'''

#매서드 체이닝
c='python'.rjust(10).upper() #문자열을 오른쪽으로 정렬하고, 대문자로 바꾼다
#print(c)

#문자열 왼쪽에 '0' 채우기
c1='35'.zfill(5) #숫자 5칸에서 왼쪽 나머지 부분을 0으로 채움
#print(c1)


#문자열 위치 찾기(주로 많이 사용함) : 문자열이 없으면 -1을 반환함
c2='apple pineapple'.find('pl') #'pl'이 있는 문자열을 찾아서 인덱스를 반환함(여러 개일 경우 왼쪽의 가장 처음인 부분을 찾아냄)
#print(c2)

c3='apple pineapple'.rfind('pl') #오른쪽에서 부터 찾기
#print(c3)

#문자열 위치 찾기(index) : 문자열이 없으면 에러남.
c4='apple pineapple'.index('pl')
#print(c4)

c5='apple pineapple'.rindex('pl')
#print(c5)

#문자열 개수 세기(특정 문자열이 몇번 나오는지 알아
c6='apple pineapple'.count('pl')
#print(c6)

#문자열의 인덱스 찾기 문제
c7='apple pineapple apple pineapple'


'''c7_index=c7.find('pl')
print(c7_index)
new_index=c7_index+2 
find1=c7[new_index:]
print(find1)
index2=find1.find('pl')
find2_index=new_index+index2
print(find2_index)'''

a='apple pineapple apple pineapple'
while True:
    a_index=a.find('pl')
    print(a_index)
    a=a.replace("pl","xx",1)
    print(a)
    if 'pl' not in a:
        break


#'pl'인덱스 찾기(find를 사용하지 않고 하기)
a ='apple pineapple apple pineapple'
'''i=0
while i<len(a):
    if a[i]=='p' and a[i+1]=='l':
        print(i, i+1)
    i += 1'''

'''for x in range(len(a)):
    if a[x:x+2]=="pl":
        print(x)'''





