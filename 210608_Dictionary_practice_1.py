'''lux = {'health':490, 'mana':334,'melee':550,"armor":18.72}
print(lux)'''

'''a= dict(b=4, c = 5)
print(a)
print(a["b"])'''


b=dict(zip(['health','mana', 'pen'],[450,560,230]))
b['mana']=650
'''print(b)'''
print(len(b))

'''c= dict([('ge',56),('geg',56),('journey',65)])
print(c)
print('ge' in c)'''

#연습문제(카밀문제)
camille={'health':575.6, 'health_regen':1.7,'mana':338.8, 'mana_regen':1.63,
         'melee':125, 'attack_damage':60, 'attack_speed':0.625, 'armor':26,
         'magic_resistance':32.1, 'movement_speed':340}

print(camille)
print(camille["health"])
print(camille["movement_speed"])

#input을 활용하여 딕셔너리 만들기
key = input("첫번줄(키)를 입력하세요 : ").split()
value = input("두번째 (값)을 입력하세요 : ").split()

dict = dict(zip(key,value))
print(dict)
print(type(dict))


