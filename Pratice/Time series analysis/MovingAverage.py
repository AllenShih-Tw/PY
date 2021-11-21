import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error
from math import sqrt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from math import sqrt

df = pd.read_csv('Train_SU63ISt.csv', nrows=11856)
df.Datetime = pd.to_datetime(df.Datetime, 
                             format='%d-%m-%Y %H:%M')
train = df[df['Datetime'] < '2013-10-31 23:59:59']
test = df[df['Datetime'] >= '2013-10-31 23:59:59']

y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['Count'].rolling(60).mean().iloc[-1]
plt.figure(figsize=(16,8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
rms = sqrt(mean_squared_error(test.Count, y_hat_avg.moving_avg_forecast))
print(rms)
plt.show()