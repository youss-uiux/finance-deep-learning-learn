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
print('The standard deviation of the dataset: ' +str(standard_deviation), '%')
# Calculating the range
range_metric = max(cpi["CPIAUCSL"]) - min(cpi["CPIAUCSL"])
# Printing the result
print('The range of the dataset: ' + str(range_metric), '%')
# Calculating the skew
skew = cpi_latest["CPIAUCSL"].skew()
# Printing the result
print('The skew of the dataset: ' + str(skew))
# Plotting the histogram of the data
fig, ax = plt.subplots()
ax.hist(cpi['CPIAUCSL'], bins = 30, edgecolor = 'black', color = 'white')
median = cpi_latest["CPIAUCSL"].median()
# Printing the result
print('The median of the dataset: ' + str(median), '%')
# Plotting the latest observations in black with a label
# Add vertical lines for better interpretation
ax.axvline(mean, color='black', linestyle='--', label = 'Mean',linewidth = 2)
ax.axvline(median, color='grey', linestyle='-.', label = 'Median',
linewidth = 2)
plt.grid()
plt.legend()
plt.show()
#plt.show()  