import pandas as pd
import numpy as np

df = pd.read_csv("jr-lr.csv")
print(df)

# df.replace(0, np.nan)
df.fillna(0, inplace=True)
# df.interpolate(inplace=True)
# df.dropna(inplace=True)
x = df.drop(columns=["f", "a", "b"], axis=1)
y = df["f"]
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)
print(lr.coef_)
print(lr.intercept_)

y_pred = lr.predict(x_test)
print(y_pred)

print("model in trainset score is:", lr.score(x_train, y_train))
print("model in testset score is:", lr.score(x_train, y_train))
