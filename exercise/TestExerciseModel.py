import pandas as pd

exerciseData = pd.read_csv("./exercise.csv")
print(exerciseData.head())
print(exerciseData.shape)
print(exerciseData.ndim)
print(exerciseData.info())

x = exerciseData[
    ["流动比率", "速动比率", "现金到期债务比", "经营活动产生的现金流量净额/流动负债", "EBITDA/利息费用", "全部债务/EBITDA", "营业利润/营业总收入", "总资产报酬率(TTM)",
     "净资产收益率ROE(平均)", "流动资产周转率", "存货周转率", "总资产周转率", "应收账款周转率", "营业收入(同比增长率)"]]
y = exerciseData["kind"]
print(x)
print(y)
print("==" * 100)
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)
print(x_train)
print("==" * 100)
print(y_train)

# 处理特征方式
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)
x_train_dv = dv.fit_transform(x_train.to_dict())
