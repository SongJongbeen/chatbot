# -*- enconding: utf-8 -*-

from konlpy.tag import Kkma
import numpy as np
from numpy import dot
from numpy.linalg import norm
import openpyxl

kkma = Kkma()
bows = []
word_dics = []
processed = []

load_xlsx = openpyxl.load_workbook('eta_assistant_results.xlsx', data_only=True)
load_sheet = load_xlsx['eta_assistant']
stop_word_list = ['날씨', '더위', '무더위', '코로나', '노고', '고생', '실례', '감사', '질문', '문의', '학교', '학우', '학생', '대부분', '울', '조', '교', '조교', '님', '여태', '안녕', '감사', '고맙', '친절', '답변', '도움', '죄송', '주신', '항상', '공유', '확인', '확인차', '차', '미', '미처', '처', '글', '아', '휴', '셈', '아이구', '아이쿠', '아이고', '어', '저', '나', '우리', '거랑', '학', '종지', '저희', '건', '휴', '인젠', '금', '좀', '이상', '허', '헉', '허걱', '매', '재', '매번', '들', '모', '너희', '당신', '그', '그것', '너', '오호', '아하', '흐흐', '쉿', '전부', '한마디', '한항목', '자', '이', '여러분', '자기', '자신', '아니', '와아', '응', '아이', '령', '영', '하', '것', '그', '되', '수', '순', '이', '보', '우선', '나', '사람', '주', '아니', '우리', '제가', '때', '시', '년', '예', '말', '일', '때문', '일과', '목란', '로', '두', '알', '더', '중', '가지', '속', '하나', '자신', '내', '데', '경우', '우와', '헐', '보통', '수고', '사항', '댓', '댓글', '졸', '예자', '부', '바', '사정상', '에타조교', '답', '대', '대신', 'ㅠㅠ', '대체적', '거', '다', '가도', '도']

range_cell = load_sheet['A1:A12718']
for row in range_cell:
    for cell in row:
        sentence = cell.value
        bow = kkma.nouns(sentence)
        for token in bow:
            if token not in stop_word_list:
                word_dics.append(token)
        processed.append(word_dics)
        word_dics = []

for i in range(len(processed)):
    load_sheet.cell(row=i+1, column=3).value = str(processed[i])

load_xlsx.save('eta_assistant_results.xlsx')
