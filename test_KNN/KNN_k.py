# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target
import numpy as np

print(np.unique(Y))

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.5)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_test = sc.fit_transform(X_train)
X_train = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt

K_scores = []  # 将k值存储在list中
lk = range(2, 30)  # 从2到30选择k值
for k in lk:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    score = cross_val_score(knn, X_test, Y_test, cv=10, scoring="accuracy")
    K_scores.append(np.mean(score))
print(K_scores)
# 绘制k值随着score的变化图像
plt.plot(lk, K_scores)
plt.xlabel("K")
plt.ylabel("Scores")
plt.show()
