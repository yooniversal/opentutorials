# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ta2SkP5vXQeTxKLm6ql3Tl9PqNHkTT9f
"""

# 라이브러리 사용
import tensorflow as tf
import pandas as pd

# 데이터 준비
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)
아이리스.head()

# 원핫인코딩
아이리스 = pd.get_dummies(아이리스)

# 독립, 종속
독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = 아이리스[['품종_setosa', '품종_versicolor', '품종_virginica']]
print(독립.shape, 종속.shape)

# 모델 만들기
X = tf.keras.layers.Input(shape=[4])
H = tf.keras.layers.Dense(8, activation="swish")(X)
H = tf.keras.layers.Dense(8, activation="swish")(H)
H = tf.keras.layers.Dense(8, activation="swish")(H)
Y = tf.keras.layers.Dense(3, activation='softmax')(H)
model = tf.keras.models.Model(X, Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')

# 모델 구조 확인
model.summary()

# 모델 학습
# verbose는 출력 OFF
model.fit(독립, 종속, epochs=1000, verbose=0)
model.fit(독립, 종속, epochs=10)

# 모델 이용
# 처음 5개
print(model.predict(독립[:5]))
print(종속[:5])

# 마지막 5개
print(model.predict(독립[-5:]))
print(종속[-5:])

# weight 과 bias 출력
print(model.get_weights)