import pandas_datareader as pdr
import matplotlib.pyplot as plt
start_date = '1950-01-01'
end_date = '2023-01-23'
cpi = pdr.DataReader('CPIAUCSL', 'fred', start_date, end_date)
print(cpi.tail())
count_nan = cpi['CPIAUCSL'].isnull().sum()
print('Number of nan values in the CPI dataframe: ' + str(count_nan))
# Transforming the CPI into a year-on-year measure
cpi = cpi.pct_change(periods = 12, axis = 0) * 100
# Dropping the nan values from the rows
cpi = cpi.dropna()
# Calculating the mean of the CPI over the last 20 years
cpi_latest = cpi.iloc[-240:]
mean = cpi_latest["CPIAUCSL"].mean()
# Printing the result
print('The mean of the dataset: ' + str(mean), '%')
# Plotting the latest observations in black with a label
plt.plot(cpi_latest[:], color = 'black', linewidth = 1.5,
label = 'Change in CPI Year-on-Year')
# Plotting horizontal lines that represent the mean and the zero threshold
plt.axhline(y = mean, color = 'red', linestyle = 'dashed',
label = 'Mean')
plt.axhline(y = 0, color = 'blue', linestyle = 'dashed', linewidth = 1)
plt.grid()
plt.legend()
# Calculating the variance
variance = cpi_latest["CPIAUCSL"].var()
# Printing the result
print('The variance of the dataset: ' + str(variance), '%')
# Calculating the standard deviation
standard_deviation = cpi_latest["CPIAUCSL"].std()
# Printing the result
print('The standard deviation of the dataset: ' +
str(standard_deviation), '%')
# Calculating the range
range_metric = max(cpi["CPIAUCSL"]) - min(cpi["CPIAUCSL"])
# Printing the result
print('The range of the dataset: ' + str(range_metric), '%')
#plt.show()  