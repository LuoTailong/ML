from sklearn.feature_extraction import DictVectorizer

v = DictVectorizer(sparse=False)
D = [{'pclass': "1st", 'age': 20, "sex": "female"},
     {'pclass': "2nd", 'age': 30, "sex": "male"},
     {'pclass': "3rd", 'age': 30, "sex": "male"}]
x = v.fit_transform(D)
print(x)
print(v.feature_names_)
