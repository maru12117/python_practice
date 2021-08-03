'''i=1
total =1
while i<=20:
    total*=2
    i += 1
print(total)'''

a = []
num = 98
while num/2>0:
    if num%2 == 0:
        result = divmod(num,2)
        num = result[0]
        a.append(0)
    else:
        result = divmod(num,2)
        num = result[0]
        a.append(1)
for x in a[-1::-1]:
    print(x, end="")


