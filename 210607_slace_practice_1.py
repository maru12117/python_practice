'''year = [2011, 2012, 2013,2014, 2015,2016,2017,2018]
popuration= [10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]

print(year[-3:])
print(popuration[-3:])'''

"""n = -32,75,97,-10,9,32,4,-15,0,76,14,2
print(n[1::2])"""

'''a = input("숫자를 입력해주세요 : ").split()
list_a = list(a)
del list_a[-5:]
print(tuple(list_a))'''

string = []
string = input("문자 2개를 입력해주세요 : ").split()

print(string[0][1::2] + string[1][0::2])
