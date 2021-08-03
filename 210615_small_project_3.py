import random
import time

keyword = ["rabbit", "elepthant","bear","dog","cat","pen","computer", "moniter"]
start=time.time()
print("==========================================================")
print("타자게임을 시작합니다")

test_num = 1
fail = 1
while test_num <=5:
    random_word=random.choice(keyword)
    while True :
        print(test_num, "번 문제 : ", random_word)
        user_word =input("정답을 입력합니다 : ")
        if random_word != user_word:
            print("오타를 확인해주세요 (오류", fail,"회 입력) \n")
            fail += 1
        else:
            print("정답입니다! \n")
            fail = 1
            break
        
    test_num += 1
    if test_num==6:
        print("다섯개를 모두 맞췄습니다!! 축하해요 \n")
        end=time.time()
        et = end-start
        et = format(et, ".2f")
        print("경과시간은 ",et,"초 입니다")

    
    


