import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#Alcohol Mean/Median/Mode/Range/Variance/StD

Alcohol_mean = df['Alcohol'].mean() 
print "The mean for the Alcohol dataset is %.2f." % Alcohol_mean

Alcohol_median = df['Alcohol'].median() 
print "The median for the Alcohol dataset is %.2f." % Alcohol_median

Alcohol_mode = stats.mode(df['Alcohol'])
#print "The mode for the Alcohol dataset is %r." % Alcohol_mode

Alcohol_range = max(df['Alcohol']) - min(df['Alcohol'])
print "The range for the Alcohol dataset is %.2f." % Alcohol_range

Alcohol_std = df['Alcohol'].std() 
print "The standard deviation for the Alcohol dataset is %.2f." % Alcohol_std

Alcohol_var = df['Alcohol'].var() 
print "The variance for the Alcohol dataset is %.2f." % Alcohol_var

#Tobacco Mean/Median/Mode/Range/Variance/StD

Tobacco_mean = df['Tobacco'].mean() 
print "The mean for the Tobacco dataset is %.2f." % Tobacco_mean

Tobacco_median = df['Tobacco'].median() 
print "The median for the Tobacco dataset is %.2f." % Tobacco_median

Tobacco_mode = stats.mode(df['Tobacco']) 
#print "The mode for the Tobacco dataset is %.2f." % Tobacco_mode

Tobacco_range = max(df['Tobacco']) - min(df['Tobacco'])
print "The range for the Tobacco dataset is %.2f." % Tobacco_range

Tobacco_std = df['Tobacco'].std() 
print "The standard deviation for the Tobacco dataset is %.2f." % Tobacco_std

Tobacco_var = df['Tobacco'].var() 
print "The variance for the Tobacco dataset is %.2f." % Tobacco_var



