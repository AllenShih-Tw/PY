from pandas_datareader import data

# Only get the adjusted close.
aapl = data.DataReader("AAPL", 
                       start='2015-1-1', 
                       end='2015-12-31', 
                       data_source='yahoo')['Adj Close']

aapl.plot(title='AAPL Adj. Closing Price')