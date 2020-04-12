
import numpy as np

# f = h5py.File("test/jr/model.v2.0.h5", 'r')  # 打开h5文件
# f.keys()  # 可以查看所有的主键
# a = f['data'][:]  # 取出主键为data的所有的键值
# f.close()
# h5py.run_tests()


import pandas as pd
import h5py
h5 = pd.HDFStore('test/jr/model.v2.0.h5', 'r')
futures_data = h5['futures_data']  # VSTOXX futures data
options_data = h5['options_data']  # VSTOXX call option data
h5.close()