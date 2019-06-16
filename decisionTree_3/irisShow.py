# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris

iris = load_iris()
# 打印
print(iris.keys())
print(iris.data)

import numpy as np

print(np.unique(iris.target))
print(iris.target)
print(iris.target_names)
print(iris.DESCR)
print(iris.feature_names)
x = iris.data
y = iris.target
# 切分数据
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)

# 训练模型
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
# 训练
dtc.fit(x_train, y_train)
print(dtc.feature_importances_)
# 预测
y_pred = dtc.predict_proba(x_test)
print(y_pred)
# 验证
print("model in train set score is:", dtc.score(x_train, y_train))
print("model in train set score is:", dtc.score(x_test, y_test))
# 可视化
from sklearn.tree import export_graphviz

export_graphviz(dtc, out_file="iris.dot", filled=True, class_names=iris.target_names,
                feature_names=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], )
