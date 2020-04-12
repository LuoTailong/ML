# 导入必要的工具包
import xgboost as xgb

# 计算分类正确率
from sklearn.metrics import accuracy_score

# read in data，数据在xgboost安装的路径下的demo目录,现在我们将其copy到当前代码下的data目录
my_workpath = '../data/'
dtrain = xgb.DMatrix(my_workpath + 'agaricus.txt.train')
dtest = xgb.DMatrix(my_workpath + 'agaricus.txt.test')

print(dtrain.num_col())
print(dtrain.num_row())
print(dtest.num_row())

# max_depth： 树的最大深度。缺省值为6，取值范围为：[1,∞]
# eta：为了防止过拟合，更新过程中用到的收缩步长。在每次提升计算之后，算法会直接获得新特征的权重。
# eta通过缩减特征的权重使提升计算过程更加保守。缺省值为0
# .3，取值范围为：[0, 1]
# silent：取0时表示打印出运行时信息，取1时表示以缄默方式运行，不打印运行时信息。缺省值为0
# objective： 定义学习任务及相应的学习目标，“binary: logistic” 表示二分类的逻辑回归问题，输出为概率。
# 其他参数取默认值。

# specify parameters via map
param = {'max_depth': 2, 'eta': 1, 'silent': 0, 'objective': 'binary:logistic'}
print(param)

# 设置boosting迭代计算次数
num_round = 2

import time

starttime = time.clock()

bst = xgb.train(param, dtrain, num_round)  # dtrain是训练数据集

endtime = time.clock()
print(endtime - starttime)

train_preds = bst.predict(dtrain)
train_predictions = [round(value) for value in train_preds]
y_train = dtrain.get_label()  # 值为输入数据的第一行
train_accuracy = accuracy_score(y_train, train_predictions)
print("Train Accuary: %.2f%%" % (train_accuracy * 100.0))

# make prediction
preds = bst.predict(dtest)

predictions = [round(value) for value in preds]

y_test = dtest.get_label()
test_accuracy = accuracy_score(y_test, predictions)
print("Test Accuracy: %.2f%%" % (test_accuracy * 100.0))

from matplotlib import pyplot
import graphviz

xgb.plot_tree(bst, num_trees=0, rankdir='LR')
pyplot.show()

xgb.plot_tree(bst, num_trees=1, rankdir='LR')
pyplot.show()
xgb.to_graphviz(bst, num_trees=0)
xgb.to_graphviz(bst, num_trees=1)

import numpy as np
np.random.randn()