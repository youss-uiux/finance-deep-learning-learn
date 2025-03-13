import pandas_datareader as pdr
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