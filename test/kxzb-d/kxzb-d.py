# -*- coding: utf-8 -*-
import pandas as pd

# 1 导入数据
sale1Data = pd.read_csv("kxzb-d.csv", sep=",", error_bad_lines=False)
sale1Data.interpolate(inplace=True)
sale1Data.dropna(inplace=True)
print(sale1Data)
print(sale1Data.shape)
print(sale1Data.ndim)
print(sale1Data.info())
print(sale1Data.head())
print(sale1Data.index)
print("------------------------")
print(sale1Data.columns)

# 遗失值插补
# from sklearn.preprocessing import Imputer
#
# my_imputer = Imputer()
# data_imputed = my_imputer.fit_transform(sale1Data)
# print(type(data_imputed))
# # array转换成df
# sale1Data_imputed = pd.DataFrame(data_imputed, columns=sale1Data.columns)
# print(sale1Data_imputed)

# 2 数据处理
# x = sale1Data.drop(columns=["发行人最新评级", "证券代码", "证券简称"], axis=1)
# y = sale1Data["发行人最新评级"]
# x = sale1Data.drop(columns=["1", "2", "3"], axis=1)
# y = sale1Data["17"]
x = sale1Data.drop(columns=["ch", "a", "b"], axis=1)
y = sale1Data["ch"]

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

dtc = DecisionTreeClassifier(criterion="entropy", max_depth=12, min_samples_leaf=2)
dtc.fit(x_train, y_train)

# 4 加载模型
# from sklearn.externals import joblib
# dtc = joblib.load("kxzb-d.pkl")

# 5 模型预测
y_pred = dtc.predict(x_test)
print(y_pred)

# 6 模型校验
# print("model in trainset score is {}".format(dtc.score(x_train, y_train)))
print("model in trainset score is %.2f" % (dtc.score(x_train, y_train)))
print("model in testset score is %.2f" % (dtc.score(x_test, y_test)))

from sklearn.metrics import confusion_matrix, classification_report

print("confusion matrix:", confusion_matrix(y_test, y_pred))
print("conputetion matrix:", classification_report(y_test, y_pred))

# 7 保存模型
from sklearn.externals import joblib

joblib.dump(dtc, "kxzb-d.pkl")

# 8 模型可视化
from sklearn.tree import export_graphviz

export_graphviz(dtc, out_file="kxzb-d.dot", feature_names=x.columns,
                class_names=["C", "CC", "A-", "A", "A+", "AA-", "AA", "AA+", "AAA"], filled=True)
