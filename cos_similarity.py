from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm
import openpyxl

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

komoran = Komoran()
bows = []
word_dics = []

load_xlsx = openpyxl.load_workbook('eta_assistant_results.xlsx', data_only=True)
load_sheet = load_xlsx['eta_assistant']

range_cell = load_sheet['A1:A4']
for row in range_cell:
    for cell in row:
        sentence = cell.value
        bow = komoran.nouns(sentence)
        for i in bow:
            bows.append(i)
for token in bow:
    if token not in word_dics:
        # if token not in stop_word_list
        word_dics.append(token)
