# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris

# 1.进行数据的读入---导入数据
iris = load_iris()
# 2.对数据进行简单的统计分析和图形化的展示 见irisShowPro
print(iris.keys())
print(iris.data)

import numpy as np

print(np.unique(iris.target))
print(iris.target)
print(iris.target_names)
print(iris.DESCR)
print(iris.feature_names)

# 3 确定特征和标签-X和y
x = iris.data
y = iris.target

# 4.1 降维---pca
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
x = pca.fit_transform(x)
print(":" * 1000)
print(x)
print(":" * 1000)
# print(pca.explained_variance_)

# 切分数据
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)

# 4 特征工程
from sklearn.preprocessing import StandardScaler, MinMaxScaler

sc = MinMaxScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

# 5 建立模型
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(x_train_std, y_train)

# 6 利用模型进行预测
y_pred = dtc.predict(x_test_std)
print(y_pred)

# 7 验证
print("model in train set score is:", dtc.score(x_train_std, y_train))
print("model in train set score is:", dtc.score(x_test_std, y_test))

# 8 可视化
from sklearn.tree import export_graphviz

export_graphviz(dtc, filled=True)
