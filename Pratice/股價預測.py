import numpy as np
import pandas as pd
# get data
import pandas_datareader as pdr
# visual
import matplotlib.pyplot as plt
#time
import datetime as datetime
#Prophet
from fbprophet import Prophet
from sklearn import metrics

code= input('Enter Stock code:  ')+('.TW')
start_date = input('Enter Start Time:  ')
start = datetime.datetime.strptime(start_date,"%Y/%m/%d")
end_date = input('Enter End Time:  ')
end = datetime.datetime.strptime(end_date,"%Y/%m/%d")
# end = (2019,12,1)
# start = datetime.datetime(2019,11,1)
df_2354 = pdr.DataReader(code, 'yahoo',start,end)
df_2354.head()
# plt.style.use('ggplot')
# df_2354['Adj Close'].plot(figsize=(10, 8));

new_df_2354 = pd.DataFrame(df_2354['Adj Close']).reset_index().rename(columns={'Date':'ds', 'Adj Close':'y'})
new_df_2354.head()

new_df_2354['y'] = np.log(new_df_2354['y'])
# 定義模型
model = Prophet()
# 訓練模型
model.fit(new_df_2354)
# 建構預測集
future = model.make_future_dataframe(periods=30) #forecasting for 1 year from now.
# 進行預測
forecast = model.predict(future)
forecast.head()

figure=model.plot(forecast)

df_2354_close = pd.DataFrame(df_2354['Adj Close'])
two_years = forecast.set_index('ds').join(df_2354_close)
two_years = two_years[['Adj Close', 'yhat', 'yhat_upper', 'yhat_lower' ]].dropna().tail(800)
two_years['yhat']=np.exp(two_years.yhat)
two_years['yhat_upper']=np.exp(two_years.yhat_upper)
two_years['yhat_lower']=np.exp(two_years.yhat_lower)
two_years[['Adj Close', 'yhat']].plot(figsize=(8, 6));


two_years_AE = (two_years.yhat - two_years['Adj Close'])
two_years_AE.describe()

print(two_years_AE.describe())
print ("MSE:",metrics.mean_squared_error(two_years.yhat, two_years['Adj Close']))
print ("MAE:",metrics.mean_absolute_error(two_years.yhat, two_years['Adj Close']))


fig, ax1 = plt.subplots(figsize=(10, 8))
ax1.plot(two_years['Adj Close'])
ax1.plot(two_years.yhat)
ax1.plot(two_years.yhat_upper, color='black',  linestyle=':', alpha=0.5)
ax1.plot(two_years.yhat_lower, color='black',  linestyle=':', alpha=0.5)

ax1.set_title(code+'-Prediction error')
ax1.set_ylabel('Price')
ax1.set_xlabel('Date')


import matplotlib
matplotlib.matplotlib_fname()

# plt.show()
plt.savefig('pic.png')