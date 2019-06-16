import pandas as pd

data = pd.read_csv("./car.csv")
print(data.shape)
print(data.ndim)
print(data.head())
print(data.info())

x = data[["Miles", "Deliveries"]]
y = data["Travel_Time"]
print(x)
print(y)
print("=" * 100)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)
print(x_train)
print(y_train)
print("=" * 100)

# 处理特征的方式
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)
x_train_dv = dv.fit_transform(x_train.to_dict(orient="records"))
x_test_dv = dv.transform(x_test.to_dict(orient="records"))
print(x_train_dv)
print(dv.feature_names_)
print(x_test_dv)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

le = LabelEncoder()
x_train_le = le.fit_transform(x_train["Deliveries"])
x_test_le = le.transform(x_test["Deliveries"])
print(x_train)
print(x_train_le)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
# dtc.fit(x_train_dv,y_train_le)
import numpy as np

print(np.version.version)
