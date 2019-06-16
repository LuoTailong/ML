import pandas as pd
import os

# 1读取数据
datapath = os.path.join(".", "tantanic.txt")
tantanic = pd.read_csv(datapath)


def show_data_info():
    print(tantanic.shape)
    print(tantanic.info())
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.catplot(x="sex", y="survived", hue="pclass", kind="bar", data=tantanic)
    plt.show()


# 调用显示图像和属性函数
show_data_info()

# 2特征工程
# 2.1特征选择
x = tantanic[["age", "pclass", "sex"]]
print(x)
y = tantanic["survived"]

# 2.2缺失值处理--age年龄列--均值插补技术
x["age"].fillna(x["age"].mean(), inplace=True)
print(x)

# 2.3切分数据
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)

# 2.4类别型变量处理
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)
x_train_dv = dv.fit_transform(x_train.to_dict(orient="records"))
x_test_dv = dv.transform(x_test.to_dict(orient="records"))
print(x_train_dv)
print(dv.feature_names_)

# 3建立模型
from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier(criterion="gini")
print(dtc.fit(x_train_dv, y_train))

# 4模型预测
y_pred = dtc.predict(x_test_dv)
print(y_pred)

# 5模型校验
print("model in trainset:", dtc.score(x_train_dv, y_train))
print("model in testset:", dtc.score(x_test_dv, y_test))
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 6可视化操作
from sklearn.tree import export_graphviz

export_graphviz(dtc, filled=True, class_names=["no", "yes"],
                feature_names=["age", "pclass_1", "pclass_2", "pclass_3", "sex_1", "sex_2"])
