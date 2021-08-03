import copy
#2차원 리스트를 카피하는 경우
a = [[10,20],[30,40],[50,60,70]]
'''b=a.copy()
b[0][1]=4
print(a)
print(b)'''
#a와b에 모두 변경된 것을 알 수 있음, 따라서 2차원 이상의 다차원 리스트를 완전히 복사하기 위해서는.
#copy모듈의 deepcopy()를 사용해야 함


b=copy.deepcopy(a)
b[0][1]=4
'''print(a)
print(b)'''

#연습문제

a =[[[0 for i in range(3)] for x in range(4)] for y in range(2) ]
#print(a)
#3차원 리스트는 높이x가로x세로 형태로 이루어져있음

#다시 연습
#[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 2차원 리스트 만들어봐라 (2가지)

c = [[0 for x in range(5)] for y in range(3)]
#print(c)

c1 = [[0*i for i in range(5)]for x in range(3)]
#print(c1)

c2=[[0 for x in range(2)] for y in range(3)]
#print(c2)

a=[3,1,3,2,5]
#[0]*3하면...[0,0,0]이된다...
c4=[[[0]*x for x in a]]
#print(c4)
c4=[[[0]*x for x in [3,1,3,2,5]]]

#[[0,0,0],[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

c5 = [[[0 for i in range(3)]for x in range(4)]for y in range(2)]
#print(c5)

c6=[0 for x in range(4)]
print(c6) #[0, 0, 0, 0]
c7=[[0]*x for x in range(4)]
print(c7) # [[], [0], [0, 0], [0, 0, 0]] 확인






