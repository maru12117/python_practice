fruits = {'apple':1000, 'banana':700, 'orange':1500,'pineapple':2000}
'''print(fruits)'''

lux = {'health':800, 'mana':334,'melee':550,'armor':18.72}
#똑같은 이름의 키가 있으면, 뒤에 있는 키의 값이 출력됨

#키에는 리스트와 딕셔너리를 사용할 수 없으나, 값에는 딕셔너리나 리스트가 가능함
x = {100:'hundred', False:0,3.5:[3.5,3.5]}

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)

#리스트나 튜플을 zip에 저장해서 나열함
lux2 = dict(zip(['health','mana', 'melee', 'armor'],[490,334,550,18.72]))

lux3 = dict([('health',490),('mana',334),('melee',550),('armor',18.72)])

lux4 = dict({'health': 490, 'mana':334,'melee':550,'armor':18.72})

#딕셔너리의 키에 접근하고 값 할당하기

lux = {'health':490, 'mana':334,'melee':550,'armor':18.72}

'''fruit_name = input("과일의 이름을 입력하세요 : ")
fruits = {'apple':1000, 'banana':700, 'orange':1500,'pineapple':2000}
fruits = dict(zip(['apple','banana','orange','pineapple'],[1000,700,1500,2000]))
print(fruits[fruit_name],"원 입니다")'''

lux['health'] = 2037
lux['mana'] = 1184

'''price = int(input("변경된 사과 가격을 입력하세요 : "))
fruits = {'apple':1000, 'banana':700, 'orange':1500,'pineapple':2000}
fruits['apple'] = price'''

#키값이 없는 것을 출력하려하면, 오류가 발생함
lux = {'health':490, 'mana':334,'melee':550,'armor':18.72}
'''print(len(lux))'''
lux['mana_regen'] = 250

'''print('health' in lux)
print('attack' in lux)'''

'''print('attack' not in lux)
print('health' not in lux)'''

'''fruits = {'apple':0, 'banana':0,'orange' :0, 'pineapple':0}
fruits_price = map(int,input("사과 바나나 오렌지 파인애플 순서로 가격을 입력해주세요 : ").split())
fruits_dict = dict(zip(list(fruits),fruits_price))
print(fruits_dict)'''

ability = input("챔피언의 새로운 능력을 입력해주세요 : ")
ability_Num = float(input("해당  능력의 수치를 입력해주세요 : "))
lux2 = dict(zip(['health','mana', 'melee', 'armor'],[490,334,550,18072]))
lux2[ability] = ability_Num
print(lux2)








