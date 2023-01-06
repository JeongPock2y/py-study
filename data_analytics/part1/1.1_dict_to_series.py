# -*- coding: utf-8 -*-

import pandas as pd

data = {'정연욱': ['남자','30','182'], '위대한' :['남자','31','175'], '한소연': ['여자','30','162'] }

df = pd.DataFrame(data, index=['1','2','3'])

print(df)
print('')