import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train_df = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

X_train = train_df.iloc[:, 0:8].values
y_train = train_df.iloc[:, 11].values
X_test = test.iloc[:, 0:8].values


# Encoding categorical train data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_train_1 = LabelEncoder()
X_train[:, 0] = labelencoder_X_train_1.fit_transform(X_train[:, 0])
labelencoder_X_train_2 = LabelEncoder()
X_train[:, 1] = labelencoder_X_train_2.fit_transform(X_train[:, 1])
labelencoder_X_train_3 = LabelEncoder()
X_train[:, 2] = labelencoder_X_train_3.fit_transform(X_train[:, 2])
labelencoder_X_train_4 = LabelEncoder()
X_train[:, 3] = labelencoder_X_train_4.fit_transform(X_train[:, 3])
labelencoder_X_train_5 = LabelEncoder()
X_train[:, 5] = labelencoder_X_train_5.fit_transform(X_train[:, 5])
labelencoder_X_train_6 = LabelEncoder()
X_train[:, 6] = labelencoder_X_train_6.fit_transform(X_train[:, 6])
onehotencoder = OneHotEncoder(categorical_features = [3])
X_train = onehotencoder.fit_transform(X_train).toarray()

# Encoding categorical test data
labelencoder_X_test_1 = LabelEncoder()
X_test[:, 0] = labelencoder_X_test_1.fit_transform(X_test[:, 0])
labelencoder_X_test_2 = LabelEncoder()
X_test[:, 1] = labelencoder_X_test_2.fit_transform(X_test[:, 1])
labelencoder_X_test_3 = LabelEncoder()
X_test[:, 2] = labelencoder_X_test_3.fit_transform(X_test[:, 2])
labelencoder_X_test_4 = LabelEncoder()
X_test[:, 3] = labelencoder_X_test_4.fit_transform(X_test[:, 3])
labelencoder_X_test_5 = LabelEncoder()
X_test[:, 5] = labelencoder_X_test_5.fit_transform(X_test[:, 5])
labelencoder_X_test_6 = LabelEncoder()
X_test[:, 6] = labelencoder_X_test_6.fit_transform(X_test[:, 6])
onehotencoder = OneHotEncoder(categorical_features = [3])
X_test = onehotencoder.fit_transform(X_test).toarray()

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#importing Keras libraries and packages
import keras
import h5py
from keras.models import Sequential
from keras.layers import Dense
from keras import backend
from keras.layers import Dropout
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.utils import np_utils

def rmse(y_true, y_pred):
	return backend.sqrt(backend.mean(backend.square(y_pred - y_true), axis=-1))

#create model
classifier = Sequential()
classifier.add(Dense(kernel_initializer = "glorot_uniform", input_dim=14, activation='relu', units = 7)) # 1st Layer
classifier.add(Dense(kernel_initializer = "glorot_uniform", activation='relu', units = 7)) # 2nd Layer
classifier.add(Dense(kernel_initializer = "glorot_uniform", activation='relu', units = 7)) # 3rd Layer
classifier.add(Dense(kernel_initializer = 'glorot_uniform', activation='relu', units = 1))
classifier.compile(loss='mse', optimizer='rmsprop', metrics=[rmse]) #changed optimizer from adam

# define the checkpoint
filepath = "weights-improvement-{epoch:02d}-{loss:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

history = classifier.fit(X_train, y_train, batch_size=32, epochs=60 ,validation_split=0.15, callbacks = callbacks_list)
#history = classifier.fit(X_train, y_train, batch_size=32, epochs=60 ,validation_split=0.15)

# plot metrics
plt.plot(history.history['rmse'])
plt.show()

scores = classifier.evaluate(X_train, y_train, verbose=0)
print("%s: %.2f%%" % (classifier.metrics_names[1], scores[1]))