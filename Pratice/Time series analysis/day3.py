import pandas as pd
from pandas import Series
import matplotlib
from matplotlib import pyplot
Series = pd.read_csv('daily-total-female-births.csv', header=0)
Series.plot()
pyplot.show()