# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Y8ZV9LRUnNE_wXoAKCLbPsQVgNF72CA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Iris_data = pd.read_csv("/content/drive/MyDrive/Machine Learning/data/iris.csv")
#Basic Information regarding data
Iris_data.info()

Iris_data.describe()

#exploring distribution plot for all features

for i in Iris_data.columns:
    if i == 'Species':
        continue
    sns.set_style('whitegrid')
    sns.FacetGrid(Iris_data,hue='Species')\
    .map(sns.distplot,i)\
    .add_legend()
    plt.show()

#mymodel
from sklearn import tree
import graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score

X = Iris_data[['SepalLengthCm', 'SepalWidthCm','PetalLengthCm', 'PetalWidthCm','Sepal_petal_wid_len_diff','Sepal_petal_width_diff']]
y = Iris_data['Species']
#split data
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.30, random_state=42)
#test and train data
Xt, Xcv, Yt, Ycv = train_test_split(Xtrain, Ytrain, test_size=0.10, random_state=42)
#Decision tree classifier
Iris_clf = DecisionTreeClassifier(criterion='gini',min_samples_split=2)
print('Accuracy score is:',cross_val_score(Iris_clf, Xt, Yt, cv=3, scoring='accuracy').mean())

#model performance on test data
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score
Y_hat = Iris_clf.predict(Xcv)
print('Accuracy score for test data is:',accuracy_score(Ycv, Y_hat))

# model performance on new data
YT_hat = Iris_clf.predict(Xtest)
print('Model Accuracy Score on new data(Xtest) is:',accuracy_score(Ytest, YT_hat)*100,'%')