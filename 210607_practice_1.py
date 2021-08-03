#거북이와 학의 총합이 8, 다리의 합이 22이면...거북이와 학은 몇마리인지..?

#총 합
nTotal = 8
#총 다리의 합
nLeg  = 22
#모든 거북이 다리의 합(모두 거북이라면)
nTurtleLeg = 4*nTotal
#거북이 다리에서 총 다리의 합을 뺸 학 다리
nHakLeg = nTurtleLeg-nLeg

#학의 다리가 2개니깐...
nHak = int(nHakLeg/2)
nTurtle = nTotal-nHak
print(nHak)
print(nTurtle)
