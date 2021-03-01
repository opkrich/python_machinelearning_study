## learning deep learning
# import tensorflow as tf
# import pandas as pd
#
# path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
# lemonade = pd.read_csv(path)
# IV = lemonade[['온도']]
# DV = lemonade[['판매량']]
#
# X = tf.keras.layers.Input(shape=[1])
# Y = tf.keras.layers.Dense(1)(X)
# model = tf.keras.models.Model(X,Y)
# model.compile(loss='mse')
#
# model.fit(IV,DV, epochs=5000)
#
# print(model.predict(IV))
# print(model.predict([[10]]))

## learning pandas
# import pandas as pd
#
# path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
# lemonade = pd.read_csv(path)
# path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
# boston = pd.read_csv(path)
# path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
# iris = pd.read_csv(path)
#
# print(lemonade.shape)
# print(boston.shape)
# print(iris.shape)
#
# print(lemonade.columns)
# print(boston.columns)
# print(iris.columns)
#
# IV = lemonade[['온도']]
# DV = lemonade[['판매량']]
# print(IV.shape, DV.shape)
#
# IV = boston[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
#        'ptratio', 'b', 'lstat']]
# DV = boston[['medv']]
# print(IV.shape, DV.shape)
#
# IV = iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
# DV = iris[['품종']]
# print(IV.shape, DV.shape)
#
# print(lemonade.head)
# print(boston.head)
# print(iris.head)