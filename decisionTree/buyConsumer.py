# -*- coding: utf-8 -*-
import pandas as pd

# 1 导入数据
buyData = pd.read_csv("buy.csv", sep=",")
print(buyData)
print(buyData.shape)
print(buyData.ndim)
print(buyData.info())
print(buyData.head())
print(buyData.index)
print(buyData.columns)

# 2 数据处理
x = buyData.drop(labels="Class:buy_computer", axis=1)
y = buyData["Class:buy_computer"]

# 3 特征工程
# 数据集切分
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# 4 建立决策树模型
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion="entropy", max_depth=6, min_samples_leaf=2)
dtc.fit(x_train, y_train)

# 5 模型预测
y_pred = dtc.predict(x_test)
print(y_pred)

# 6 模型校验
# print("model in trainset score is {}".format(dtc.score(x_train, y_train)))
print("model in trainset score is %.2f" % (dtc.score(x_train, y_train)))
print("model in trainset score is %.2f" % (dtc.score(x_test, y_test)))

from sklearn.metrics import confusion_matrix, classification_report

print("confusion matrix:", confusion_matrix(y_test, y_pred))
print("conputetion matrix:", classification_report(y_test, y_pred))

# 7 保存模型
from sklearn.externals import joblib

joblib.dump(dtc, "buy.pkl")

# 8 模型可视化
from sklearn.tree import export_graphviz

export_graphviz(dtc, out_file="buy.dot", feature_names=x.columns, class_names=["no", "yes"], filled=True)
