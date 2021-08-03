#서식 지정자로 문자열 넣기(%s는 문자열이라는 뜻이며, String의 s)
print('I am %s.' % 'James')

name='maria'
print('I am %s.' % name)

#서식 지정자 vs 포매팅
# %d % 숫자를 활용하여 숫자넣음
print('I am %d years old' % 20)

# %f 는 실수를 활용함
print('%f' % 2.3)

print('%.2f' % 2.3) #소수점 3자리까지 출력

print('%10s' % 'Python') #오른쪽 정렬(칸10개 만들어서)
print('%-10s' % 'Python') #왼쪽 정렬(칸10개 만들어서)

print('Today is %d %s.' % (2, 'April')) #가로를 활용하여 구분
print('Today is %d%s.' % (2, 'April'))

print('Hello, {0}'.format('world!')) #foramtting하는 값이 {0}안으로 들어감
print('Hello, {2},{0},{1}'.format(100,200,'Hi')) #포맷에 지정된 인덱스 순서대로 넣음

print('Hello, {0}{0}{0} {1}{1}{1}'.format('a','b'))

print('Hello, {} {} {} '.format('Python','Script',3.6))

#변수를 지정하여 인덱스 대신 넣을 수도 있음
print('Hello, {language}.{version}'.format(language='Python', version=3.6))

language='Python'
version=3.6
print(f'Hello, {language} {version}')

#정렬을 할 방향과 길이를 지정하여 문자열을 정렬한다
print('{0:<10}'.format('python')) #왼쪽 정렬, 칸은 10개를 만듦
print('{0:>10}'.format('python')) #오른쪽 정렬, 칸은 10개를 만듦

print('{0:<10} {2:>10}{1:<10}'.format('python','abc',123)) #0,1,2는 format의 인덱스부분

print('%03d' % 1)
print('{0:03d}'.format(35)) #0번쨰 format, 000이고, 숫자이며, 총 3칸을 활용함
print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37)) # '.'까지 포함해서 총 8칸

print('{0:0<10}'.format(15)) #길이 10, 왼쪽으로 정렬하고 남은 공간은 0으로 채움
print('{0:>10}'.format(15))
print('{0:x>10.2f}'.format(15)) #길이 10, 오른쪽으로 정렬하고 소수점 2까지 채움, 남은공간은 1로 채움

#
print('{0:>10}'.format(15)) #남은 부분을 빈칸으로 채움
print('{0:1>10}'.format(15)) #남은 부분을 1로 채움
print('{1:x>10}'.format(15,35)) #남은 부분을 x로 채움4

path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-32\\data.txt'
path_list=path.split('\\') #동일하게 있는 부분을 나누어야 함
print(path_list)
print(path_list[-1])










