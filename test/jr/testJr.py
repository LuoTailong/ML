# -*- coding: utf-8 -*-
import pandas as pd

# 1 导入数据
sale1Data = pd.read_csv("jr-decision.csv", sep=",", error_bad_lines=False)
sale1Data.fillna(0, inplace=True)
sale1Data.dropna(inplace=True)
x = sale1Data.drop(columns=["f", "a", "b"], axis=1)
y = sale1Data["f"]

# 3 特征工程
# 数据集切分
# from sklearn.model_selection import train_test_split

# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# 4 加载模型
from sklearn.externals import joblib

dtc = joblib.load("jr.pkl")

# 5 模型预测
y_pred = dtc.predict(x)
print(y_pred)
# 6 模型校验
# print("model in trainset score is {}".format(dtc.score(x_train, y_train)))
# print("model in trainset score is %.2f" % (dtc.score(x_train, y_train)))
# print("model in testset score is %.2f" % (dtc.score(x_test, y_test)))
print("model in dataset score is %.2f" % (dtc.score(x, y)))

from sklearn.metrics import confusion_matrix, classification_report

print("confusion matrix:", confusion_matrix(y, y_pred))
print("conputetion matrix:", classification_report(y, y_pred))
