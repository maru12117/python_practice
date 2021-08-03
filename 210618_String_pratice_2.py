#연습 심화문제

word = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
word_List=word.replace(",","").replace(".","").split()
#먼저 ",", "."을 ""로 만들어서 지운 후에.... 리스트를 나누어 변수를 지정함
print(word_List)
print(word_List.count('the'))

ting = 5
print("오늘의 강수량은 %d 입니다" % ting)

   
