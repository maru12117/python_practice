'''print('Python' and True)
#단락평가가 이루어진 마지막 부분에서 평가가 완료된다
print(True and 'Python')
#and 연산자가 두번쨰 값까지 확인하므로, 두번쨰 값이 반환됨
print('Python' and False)

print(False and 'Python')
#0이 False이기 떄문에 바로 0으로 그대로 나옴
print(0 and 'Python')

#바로 True에서 확인이 가능하기 떄문에 True로 판단
print(True or 'Python')
#'Python'에서 바로 True이기 떄문에 그대로 'Python'이 나옴
print('Python' or True)


print(False or 'Python')
print(0 or False)'''

#단락평가는 첫번쨰 값만으로 결과가 확실할때 두번째 값은 확인하지 않는 방법을 의미한다

#모든 점수는 50점 이상이여야 하기 때문에 and를 활용하여 모두 50이 아니면 False로 나오게 출력한다
'''korean = 92
english = 47
mathematics = 86
science = 81
print(korean>50 and english>50 and mathematics>50 and science>50)'''

korean, english, math, science = map(int,input("국어 영어 수학 과학 순서대로 점수를 입력해주세요: ").split())
print(korean>=90 and english >80 and math>85 and science>=80)

