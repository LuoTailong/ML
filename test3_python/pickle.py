# -*- coding: utf-8 -*-
import pandas as pd

original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
print(original_df)

pd.to_pickle(original_df, "./dummy.pkl")
print(pd.read_pickle("./dummy.pkl"))
