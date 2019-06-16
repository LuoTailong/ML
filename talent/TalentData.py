import pandas as pd
import os

datapath = os.path.join(".", "train.csv")
talentData = pd.read_csv(datapath)
print(talentData.head())
print(talentData.shape)
print(talentData.shape[0])
print(talentData.shape[1])
print(talentData.info())

import matplotlib.pyplot as plt
import seaborn as sns

# 分析离职和受教育程度的分析
sns.countplot(x="Attrition", hue="Education", data=talentData)
plt.show()
plt.figure(figsize=(20, 20))
# 离职和年龄的关系

# 离职和家庭距离的关系
plt.subplot(222)
# 离职和受教育程度的关系
# 离职和月收入的关系
# 离职和曾经工作的关系
