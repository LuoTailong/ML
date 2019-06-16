# -*- coding: utf-8 -*-
import pandas as pd

file = pd.read_csv("./SklearnTest.txt")
# 数据处理
new_data = file.query("is_date==-1")
data = file.query("is_date!=-1")
print(new_data)
print(data)

# 将data已经处理好的数据分为x和y
x = data.drop("is_date", axis=1)
y = data["is_date"]

# 进行切分
from sklearn.model_selection import train_test_split

# random_state = 9随机数种子 如果指定随机数种子 保证每次切分的时候结果可重复性
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=9)

# 训练模型
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)
print(dtc.feature_importances_)

# 预测
y_pred = dtc.predict(x_test)
print(x_test)
print(y_test)
print(y_pred)

# 校验
print("model in train set score is:", dtc.score(x_train, y_train))
print("model in test set score is:", dtc.score(x_test, y_test))
from sklearn.metrics import classification_report, confusion_matrix

print("classification_report score is:", classification_report(y_test, y_pred))
print("confusion_matrix score is:", confusion_matrix(y_test, y_pred))

# 可视化
from sklearn.tree import export_graphviz

export_graphviz(dtc, out_file="love.dot", feature_names=x.columns, filled=True, class_names=["no", "yes"])
# y_pred.to_csv("result.txt", sep=",")
