# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target
import numpy as np

print(np.unique(Y))

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.2)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_test = sc.fit_transform(X_train)
X_train = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3,
                           weights='uniform', algorithm='kd_tree', leaf_size=30, )
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
print(knn.score(X_test, Y_test))

from sklearn.metrics import classification_report

print(classification_report(Y_test, Y_pred))

from sklearn.cross_validation import cross_val_score

score = cross_val_score(knn, X_test, Y_test, cv=10, scoring="accuracy")
print("均值；", np.mean(score), "+ -方差：", np.std(score))
