# Kolmogorov-Smirnov Test by hand


# LIBRARIES
import pandas as pd
import numpy as np
from tabulate import tabulate
from matplotlib import pyplot
##from statsmodels.distributions.empirical_distribution import ECDF

# READ DATA
df = pd.read_excel(r'../docs/non_parametric_methods.xlsx',
                   sheet_name = 'Лист3')
print(df, '\n')

x = np.array(df['sample1'].dropna())
y = np.array(df['sample2'].dropna())
x = x.reshape((len(x),1))
y = y.reshape((len(y),1))


# FIND SUPREMUM |F(x)-G(x)|
# concatenated dataset of x and y
x_and_y = np.concatenate((x, y))
x_and_y = np.sort(x_and_y, axis=0)

# supremum is defined on [min_cdf, max_cdf] interval 
min_cdf = max(min(x), min(y))
max_cdf = min(max(x), max(y))

# count number of values of x_and_y from min_cdf to max_cdf  
num_MinToMax = ((min_cdf <= x_and_y) &
                (x_and_y <= max_cdf)).sum()

# build an array of values between min_cdf and max_cdf
# in x_and_y
MinToMax = np.ones((num_MinToMax, 1))
j = 0
for i in range(len(x_and_y)):
    if ((min_cdf <= x_and_y[i]) and
        (x_and_y[i] <= max_cdf)):
        MinToMax[j] = x_and_y[i] # add an element
        j = j + 1

# count ECDF for sample x
F_x = np.ones((num_MinToMax, 1))
for i in range(num_MinToMax):
    sum_x = 0
    for j in range(len(x)):
        if x[j] <= MinToMax[i]:
            sum_x = sum_x + 1
    F_x[i] = sum_x / len(x)

# count ECDF for sample y
F_y = np.ones((num_MinToMax, 1))
for i in range(num_MinToMax):
    sum_y = 0
    for j in range(len(y)):
        if y[j] <= MinToMax[i]:
            sum_y = sum_y + 1
    F_y[i] = sum_y / len(y)

# array of differences
dif = abs(np.subtract(F_x, F_y))

# find maximal value of an array of differences
stat = float(max(dif))


# VISUALIZE ALL DATA ANALITICALLY
results = [(x, y, x_and_y, MinToMax, F_x, F_y, dif, stat)]
print(tabulate(results, headers=["x", "y", "x_and_y",
                                 "MinToMax", "F_x",
                                 "F_y", "dif", "KS"]))


# VISUALIZE EMPIRICAL CDFs
pyplot.boxplot((x,y), labels=('x','y'))

##ecdf_x = ECDF(x)
####ecdf_y = ECDF(y)
##pyplot.plot(ecdf.x)
####pyplot.plot(ecdf.y)
pyplot.show()
