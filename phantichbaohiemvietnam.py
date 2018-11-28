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
#
df=xl
print(df.columns)
x=df.iloc[:,0]
y=df.iloc[:,1]
z=df.iloc[:,2]

# #x = sm.add_constant(x)
# #y =ax + b voi b la hang so
model = sm.OLS(y,statsmodels.tools.add_constant(x))
models=model.fit()
# new_x=[2010,2013,2014,2015,2018]
# y_predict = models.predict(new_x)
print(models.summary())
print(models.params[0])
print(models.params[1])
#thu bao hiem
#y=Nam*3.053e+4 -6.127e+07
# xy=list(x).append(2018)
#
model = sm.OLS(z,statsmodels.tools.add_constant(x))
models=model.fit()
# new_x=[2010,2013,2014,2015,2018]
# y_predict = models.predict(new_x)
print(models.summary())
print(models.params[0])
print(models.params[1])
#chi bao hiem
#z=Nam*2.577e+04 -5.171e+07

# print(2018*models.params[1]+models.params[0])
# y1=xy*models.params[1]+models.params[0]
#
# model1 = sm.OLS(z,statsmodels.tools.add_constant(x))
# models=model1.fit()
# print(models.summary())
# print(models.params[0])
# print(models.params[1])
# print(2018*models.params[1]+models.params[0])
#
#
# z1=xy*models.params[1]+models.params[0]
# print('===')
# print(x)
# print('====')
# # x1=df.iloc[4:,0]
# # y1=df.iloc[4:,1]
# # model1 = sm.OLS(y1,statsmodels.tools.add_constant(x1))
# # models1=model1.fit()
# # z1=x1*models1.params[1]+models1.params[0]
# # print(models1.summary())
# # print(models1.params[0])
# # print(models1.params[1])
# # print(2018*models1.params[1]+models1.params[0])
# fig=plt.figure()
# ax = fig.add_subplot(111)
# plt.plot( x,y1,'black',x,z1,'r--')
# ax.set_xlabel("Năm")
# ax.set_ylabel("Tong Thu Chi")
# ax.set_title("Tong Thu Chi Bao Hiem")
# ax.ticklabel_format(useOffset=False)
# plt.show()
# fig.savefig('dulieu.pdf')
# plt.close(fig)
