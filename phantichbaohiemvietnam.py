# -*- coding: utf-8 -*-
"""
Demo of unicode support in text and labels.
"""
from __future__ import unicode_literals
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import statsmodels
matplotlib.rc('font', family='Arial')
xl=pd.read_excel('solieu.xls')
df=xl
print(df.columns)
x=df.iloc[:,0]
y=df.iloc[:,1]
z=df.iloc[:,2]

model = sm.OLS(y,statsmodels.tools.add_constant(x))
models=model.fit()

print(models.summary())
print(models.params[0])
print(models.params[1])

model = sm.OLS(z,statsmodels.tools.add_constant(x))
models=model.fit()

print(models.summary())
print(models.params[0])
print(models.params[1])
