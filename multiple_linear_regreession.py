# Multiple linear regression

# After that we can devide a sample into 2 samples, use
# some criterion for outliers detection, calculate F-ratio
# and correletion coefficient r and find a confidence
# interval for correletion coefficient
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
# import statistics

df = pd.read_excel(r'D:\Statistics\отчеты тервер\sample1.xlsx', sheet_name = 'Лист1')
data = np.matrix(df)

print('Input sample (n = ' + str(data.size) + '): \n' + str(df))

# Calculate mean and std
print('mean = ' + str(data.mean()))
print('std = ' + str(np.std(data)))
print('Shape: ' + str(data.shape)) 

# Devide an input sample into 2 samples
# Input sample (20, 5) so if we devide it by 2, we get 2 samples (10, 5)
sample_1 = data[0:10, :]
sample_2 = data[10:, :]
print('\nSample 1 (n = ' + str(sample_1.size) + '): \n' + str(sample_1))
print('Shape of sample 1: ' + str(sample_1.shape))
print('\nSample 2 (n = ' + str(sample_2.size) + '): \n' + str(sample_2))
print('Shape of sample 2: ' + str(sample_2.shape))

# Comparison of two means and variances

# F-test of equality of variances
print('\nF-test of equality of variances')
print('mean_1 = ' + str(sample_1.mean()))
print('mean_2 = ' + str(sample_2.mean()))
print('Var_1 = ' + str(sample_1.var()))
print('Var_2 = ' + str(sample_2.var()))
f = sample_1.var() / sample_2.var()
print('F = Var_1/Var_2 = ' + str(f))
