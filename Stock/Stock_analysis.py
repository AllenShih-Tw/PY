import pandas
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime as datetime

date = datetime.datetime(2021,4,1)
df_2330 = pdr.DataReader('2330.TW', 'yahoo', start=date)
df_2492 = pdr.DataReader('2492.TW', 'yahoo', start=date)
df_3045 = pdr.DataReader('3045.TW', 'yahoo', start=date)
df_2412 = pdr.DataReader('2412.TW', 'yahoo', start=date)

df_total = pd.concat([df_2330['Adj Close'],df_2492['Adj Close'],df_3045['Adj Close'],df_2412['Adj Close']], axis=1)
df_total.columns=['2330', '2492', '3045', '2412']
stock_average = df_total.pct_change().corr()#日收益率平均
stock_relation = df_total.pct_change().corr()#日收益率相關分析

print(stock_relation)
