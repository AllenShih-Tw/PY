import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 10000)

plt.hist(x, bins=30, density=True, alpha=0.5,
         histtype='stepfilled', color='steelblue', edgecolor='none')

plt.show()
