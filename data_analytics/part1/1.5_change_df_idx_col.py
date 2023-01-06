# -*- coding: utf-8 -*-

import pandas as pd

# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[30, '남', '182'], [30, '여', '162'],[30, '남', '182']], 
                   index=['준서', '예은','연욱'],
                   columns=['나이', '성별', '학교'])

# 행 인덱스, 열 이름 확인하기
print(df)            #데이터프레임
print('\n')

df.to_csv("test1.csv",encoding="utf-8-sig")