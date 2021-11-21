#https://ithelp.ithome.com.tw/articles/10207621
import numpy as np
import pandas as pd
# get data
import pandas_datareader as pdr
# visual
import matplotlib.pyplot as plt
import seaborn as sns
#time
import datetime as datetime
import pandas_datareader.data as web
import datetime as dt

start = dt.datetime(2010, 12, 1)
end = dt.datetime(2019, 12, 31)

df_2330 = pdr.DataReader('1504.TW', 'yahoo', start,end)
df_2492 = pdr.DataReader('2492.TW', 'yahoo', start,end)
df_3045 = pdr.DataReader('3045.TW', 'yahoo', start,end)
df_2412 = pdr.DataReader('2412.TW', 'yahoo', start,end)

df_2330 = pdr.DataReader('1504.TW', 'yahoo', start,end)
df_AAPL = pdr.DataReader('TSLA', 'yahoo', start,end)
# data = web.DataReader('DJIA','fred', start, end)

# df_total = pd.concat([df_2330['Adj Close'],df_2492['Adj Close'],df_3045['Adj Close'],df_2412['Adj Close']], axis=1)
# df_total.columns=['2330', '2492', '3045', '2412']
df_total = pd.concat([df_AAPL['Adj Close'],df_2330['Adj Close']], axis=1)
df_total.columns=['AAPL', '2330']


print(df_total.pct_change().corr())

