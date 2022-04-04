# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OYJKkVTKGn2wDgg0-9QDHssoikG5klET
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

colnames=["sepal_length_in_cm", "sepal_width_in_cm","petal_length_in_cm","petal_width_in_cm", "class"]

#Read the dataset
dataset = pd.read_csv("/content/drive/MyDrive/Machine Learning/data/iris_2.csv", header = None, names= colnames )

#Data
dataset.head()

X = dataset.iloc[:,:-1]
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#mymodel 
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
# fit
classifier.fit(X_train, y_train)
#predict
y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print((accuracies.mean()*100))