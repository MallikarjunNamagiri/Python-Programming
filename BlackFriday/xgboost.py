
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train_df = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#handling the missing values in Product_Category_2 &3 variables
train_df['Product_Category_2'] = train_df['Product_Category_2'].fillna(train_df['Product_Category_2'].mean())
train_df['Product_Category_3'] = train_df['Product_Category_3'].fillna(train_df['Product_Category_3'].mean())

test['Product_Category_2'] = test['Product_Category_2'].fillna(test['Product_Category_2'].mean())
test['Product_Category_3'] = test['Product_Category_3'].fillna(test['Product_Category_3'].mean())

X_train = train_df.iloc[:, 0:11].values
y_train = train_df.iloc[:, 11].values
X_test = test.iloc[:, 0:11].values

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

# Avoiding the Dummy Variable Trap
X_train = X_train[:, 1:]
X_test = X_test[:, 1:]


# In[4]:

import os
mingw_path = 'C:\\Program Files\\mingw-w64\\x86_64-5.3.0-posix-seh-rt_v4-rev0\\mingw64\\bin'
os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']
os.environ['PATH'] = mingw_path + ';' + os.environ['PATH']


# In[6]:

# Fitting XGBoost to the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier()
#classifier.fit(X_train, y_train)


# In[7]:

classifier.fit(X_train, y_train)


# In[ ]:



