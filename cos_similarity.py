from konlpy.tag import Kkma
import numpy as np
from numpy import dot
from numpy.linalg import norm
import openpyxl
import time

def cos_sim(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}

    for word in word_dics:
        freq_mat[word] = 0

    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1

    return freq_mat

def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    return vec

start = time.time()

bows = []
word_dics = []
idx_link = {}
idx = -1
link = []
stop_word_list = ['날씨', '더위', '무더위', '코로나', '노고', '고생', '실례', '감사', '질문', '문의', '학교', '학우', '학생', '대부분', '울', '조', '교', '조교', '님', '여태', '안녕', '감사', '고맙', '친절', '답변', '도움', '죄송', '주신', '항상', '공유', '확인', '확인차', '차', '미', '미처', '처', '글', '아', '휴', '셈', '아이구', '아이쿠', '아이고', '어', '저', '나', '우리', '거랑', '학', '종지', '저희', '건', '휴', '인젠', '금', '좀', '이상', '허', '헉', '허걱', '매', '재', '매번', '들', '모', '너희', '당신', '그', '그것', '너', '오호', '아하', '흐흐', '쉿', '전부', '한마디', '한항목', '자', '이', '여러분', '자기', '자신', '아니', '와아', '응', '아이', '령', '영', '하', '것', '그', '되', '수', '순', '이', '보', '우선', '나', '사람', '주', '아니', '우리', '제가', '때', '시', '년', '예', '말', '일', '때문', '일과', '목란', '로', '두', '알', '더', '중', '가지', '속', '하나', '자신', '내', '데', '경우', '우와', '헐', '보통', '수고', '사항', '댓', '댓글', '졸', '예자', '부', '바', '사정상', '에타조교', '답', '대', '대신', 'ㅠㅠ', '대체적', '거', '다', '가도', '도']

kkma = Kkma()
load_xlsx = openpyxl.load_workbook('eta_assistant_results.xlsx', data_only=True)
load_sheet = load_xlsx['eta_assistant']

range_cell = load_sheet['B1:B12718']

for row in range_cell:
    for cell in row:
        link.append(cell.value)


range_cell = load_sheet['C1:C14766']
given_sentence = input('질문을 입력하세요: ')
bow2 = kkma.nouns(given_sentence)

for i in bow2:
    if i in stop_word_list:
        bow2.remove(i)

for row in range_cell:
    for cell in row:
        bow1 = cell.value
        bow1 = bow1.replace('[', '').replace(']', '').replace(',','').replace('\'', '')
        bow1 = bow1.split()
        for i in bow1:
            bows.append(i)


for token in bows:
    if token not in word_dics:
        word_dics.append(token)

freq_list2 = make_term_doc_mat(bow2, word_dics)
doc2 = np.array(make_vector(freq_list2))

for row in range_cell:
    for cell in row:
        idx += 1
        bow1 = cell.value
        freq_list1 = make_term_doc_mat(bow1, word_dics)
        doc1 = np.array(make_vector(freq_list1))
        r1 = cos_sim(doc1, doc2)
        idx_link[idx] = r1


for k, v in idx_link.items():
    if max(idx_link.values()) == v:
        print(link[k])

print('time: ', time.time() - start)
