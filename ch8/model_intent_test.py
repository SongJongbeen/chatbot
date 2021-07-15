from Preprocess import Preprocess
from IntentModel import IntentModel

p = Preprocess(word2index_dic='chatbot_dict.bin',
               userdic='user_dic.tsv')

intent = IntentModel(model_name='intent_model.h5', proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)

