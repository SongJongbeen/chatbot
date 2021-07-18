# -*- coding: utf-8 -*-

# 빠른 속도와 보통의 정확도를 원한다면 "Komoran" 또는 "Hannanum"
# 속도는 느리더라도 정확하고 상세한 품사 정보를 원한다면 "Kkma"
# 어느 정도의 띄어쓰기 되어 있는 "인터넷" 영화평/상품명을 처리할 땐 "Okt"
# 출처: https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221337575742

sentence = '네 당연히 가능하고, 들으시면 2021-1학기 성적으로 들어갑니다. 계절학기 수강 제한에 대해서는 이번에 올라온 계절학기 공지(학사공지) 사항 첨부파일 확인하셔도 나와 있고 수강편람에도 나와 있습니다~'
print(sentence)

from konlpy.tag import Hannanum, Kkma, Komoran, Okt

print("\nKomoran")
komoran= Komoran()
print(komoran.morphs(sentence))

print("\nHannanum")
hannanum= Hannanum()
print(hannanum.morphs(sentence))

print("\nOkt")      
okt= Okt()
print(okt.morphs(sentence))

print("\nKkma")
kkma= Kkma()
print(kkma.morphs(sentence))
