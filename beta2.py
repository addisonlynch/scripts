from pandas.io.data import DataReader
from datetime import datetime
from datetime import date
import numpy

### Enter the stocks to be analyzed

s1 = input('Input the first ticker in quotations: ')
s2 = input('Input the second ticker in quotations: ')


### Pulling stock data from yahoo finance

today = date.today()

stock_one = DataReader((s1),'yahoo', datetime(2013,1,1), today)
stock_two = DataReader((s2),'yahoo', datetime(2013,1,1), today)

a = stock_one['Adj Close']
b = stock_two['Adj Close']

### Calculating the beta for the stock

covariance = numpy.cov(a,b)[0][1]
variance = numpy.var(a)

beta = covariance / variance

print 'The beta for your stock is ' + str(beta)
