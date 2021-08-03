#연습문제1(평균 값을 구해라)

'''maria={'korea':94,'english':91,'mathmatics':89,'science':83}
total=0
for x in maria.values():
    total += x
print(len(maria))
avg = total/len(maria)
print(avg)'''

#심화문제
string=input("문자열 여러가지를 입력해주세요: ").split()
int_list = map(int,input("문자열 여러가지를 입력해주세요: ").split())
new_dic = dict(zip(string,int_list))

x = {a:b for a,b in new_dic.items() if a !='delta' and b!=30}
print(x)

