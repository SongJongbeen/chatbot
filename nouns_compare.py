from konlpy.tag import Komoran
from konlpy.tag import Okt
from konlpy.tag import Kkma
import numpy as np
from numpy import dot
from numpy.linalg import norm
import openpyxl

komoran = Komoran()
okt = Okt()
kkma = Kkma()

load_xlsx = openpyxl.load_workbook('test.xlsx', data_only=True)
load_sheet = load_xlsx['eta_assistant']

range_cell = load_sheet['A1:A4']
for row in range_cell:
    for cell in row:
        sentence = cell.value
        komoran_nouns = komoran.nouns(sentence)
        okt_nouns = okt.nouns(sentence)
        kkma_nouns = kkma.nouns(sentence)
        print('komoran: ', komoran_nouns)
        print('okt: ', okt_nouns)
        print('kkma: ', kkma_nouns)
