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
stop_word_list = ['안녕하세요']

range_cell = load_sheet['A1:A180']
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
