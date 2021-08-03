
'''name = 'maria'
print('I am %s.' %name)

print('I am %d years old' % 20)
print(' %d int' % 2.3)

print('%-10s' % 'python')

print('Today is %d%s' % (3, 'April'))
print('Hell {0}'.format(100))

print('Hello {0} {3} {2} {1}'.format("hi",'nihao','reshi','pengyou'))

print("{}  {}".format("hi","nihao"))

print("i am {name} {year}".format(name="maria",year=12))

language="python"
version=4.7
url=f"helle {language} {version}" #format했다는 뜻으로 간단하게 문자열 앞에다가 f를 삽입함
print(url)

print("{0:>20}".format('python')) #시작 인덱스를 지정하고 칸 10개를 만들어서 오른쪽 정렬
print("{0:<10}".format('python')) #칸 10개를 만들어서 왼쪽  정렬'''

'''print("%03d" %35) #3자리

print("{0:03d}".format(54))

print("%08.2f" % 3.6) #문자열은 8개 중에 소수점 2개 나옴
print("{0:08.3f}".format(3.569))

print("{0:$>10}".format(65)) #나머지 부분은 $로 채우기'''

path = "C:\Program Files\McAfee\MPF"
a=path.split('\\')

a1=path.replace("MPF","ADC")
print(a1)


