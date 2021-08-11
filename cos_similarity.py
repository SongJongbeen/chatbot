from konlpy.tag import Kkma
import numpy as np
from numpy import dot
from numpy.linalg import norm
import openpyxl
import time

# 각 함수들은 수학적인 내용이라 나도 잘 모름..ㅎㅎ...

# 코사인 유사도 계산 방법으로 벡터 거리를 계산
def cos_sim(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# 단어의 빈도수와 벡터 상의 밀집도 계산
def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}

    for word in word_dics:
        freq_mat[word] = 0

    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1

    return freq_mat

# 각 단어들을 벡터 공간에 위치시킴
def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    return vec

# 시간 재는 용도. start
start = time.time()

bows = [] # 
word_dics = [] 
idx_link = {}
idx = -1
link = []
# 불용어: 이 리스트 안에 있는 애들은 유사도 계산에서 고려하지 않음. -> 의미없는 데이터
stop_word_list = ['날씨', '더위', '무더위', '코로나', '노고', '고생', '실례', '감사', '질문', '문의', '학교', '학우', '학생', '대부분', '울', '조', '교', '조교', '님', '여태', '안녕', '감사', '고맙', '친절', '답변', '도움', '죄송', '주신', '항상', '공유', '확인', '확인차', '차', '미', '미처', '처', '글', '아', '휴', '셈', '아이구', '아이쿠', '아이고', '어', '저', '나', '우리', '거랑', '학', '종지', '저희', '건', '휴', '인젠', '금', '좀', '이상', '허', '헉', '허걱', '매', '재', '매번', '들', '모', '너희', '당신', '그', '그것', '너', '오호', '아하', '흐흐', '쉿', '전부', '한마디', '한항목', '자', '이', '여러분', '자기', '자신', '아니', '와아', '응', '아이', '령', '영', '하', '것', '그', '되', '수', '순', '이', '보', '우선', '나', '사람', '주', '아니', '우리', '제가', '때', '시', '년', '예', '말', '일', '때문', '일과', '목란', '로', '두', '알', '더', '중', '가지', '속', '하나', '자신', '내', '데', '경우', '우와', '헐', '보통', '수고', '사항', '댓', '댓글', '졸', '예자', '부', '바', '사정상', '에타조교', '답', '대', '대신', 'ㅠㅠ', '대체적', '거', '다', '가도', '도']

# 꼬꼬마라는 이름의 형태소 분석기
kkma = Kkma()
# openpyxl을 활용해서 데이터가 담겨져있는 엑셀 파일을 열기
load_xlsx = openpyxl.load_workbook('eta_assistant_results.xlsx', data_only=True)
load_sheet = load_xlsx['eta_assistant']

# 엑셀 파일에 담겨져있는 데이터
# A열: 원본 텍스트 / B열: A열 데이터의 출처링크 / C열: A열 데이터의 파싱된 값

# B열에 있는 각 글들의 링크들을 link에 저장함 (이 부분 따로 떼어내서 실행시간 줄여도 좋을듯?)
range_cell = load_sheet['B1:B12718']

for row in range_cell:
    for cell in row:
        link.append(cell.value)
        

# C열에 있는 파싱된 데이터들 가져옴
range_cell = load_sheet['C1:C14766']
# input을 통해 문장을 입력받음
given_sentence = input('질문을 입력하세요: ')
# 입력받은 문장을 명사 단위로 파싱함
bow2 = kkma.nouns(given_sentence)

# 명사 단위로 파싱한 결과에서 위에서 설정한 불용어에 해당하는 결과를 제거
for i in bow2:
    if i in stop_word_list:
        bow2.remove(i)

# C열에 있는 명사단위로 파싱한 데이터를 split해준 후 각각의 리스트(bow1)를 bows라는 리스트에 저장함
for row in range_cell:
    for cell in row:
        bow1 = cell.value
        bow1 = bow1.replace('[', '').replace(']', '').replace(',','').replace('\'', '')
        bow1 = bow1.split()
        for i in bow1:
            bows.append(i)

# bows에 있는 단어들을 word_dics에 넣어 중복되는 단어는 제거함.
for token in bows:
    if token not in word_dics:
        word_dics.append(token)

# 각각을 벡터 공간 상에 위치시킴
freq_list2 = make_term_doc_mat(bow2, word_dics)
doc2 = np.array(make_vector(freq_list2))

# idx를 하나씩 늘려가면서 idx_link라는 딕셔녀리에 {'인덱스':'코사인유사도'}쌍을 넣음
for row in range_cell:
    for cell in row:
        idx += 1
        bow1 = cell.value
        # 파싱된 input문장과 파싱된 각 데이터 간의 코사인 유사도를 계산함.
        freq_list1 = make_term_doc_mat(bow1, word_dics)
        doc1 = np.array(make_vector(freq_list1))
        r1 = cos_sim(doc1, doc2)
        idx_link[idx] = r1

# idx_link의 value중에 가장 높은 것(즉, 코사인 유사도가 가장 높은 것)의 idx를 구하고, 해당 idx에 해당하는 link를 출력
for k, v in idx_link.items():
    if max(idx_link.values()) == v:
        print(link[k])

# 실행시간 체크, end
print('time: ', time.time() - start)

'''
보충설명.
문장 간의 유사도를 계산할 때는 다음의 순서를 따름.
비교 대상이 될 문장을 명사 단위로 나눔.
나눠진 명사들을 벡터 공간에 위치시킴.
주어진 문장 또한 명사 단위로 나누고, 벡터 공간에 위치시킴.
각 명사들의 벡터 공간 상의 거리를 코사인을 활용해 구함.
'''
