from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

#Combine 4x Loans Data csv files
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import glob

#Combine 4x Loans Data csv files
LD = open("out.csv","a")
# first file:
for line in open("loanstats31.csv"):
    LD.write(line)
# now the rest:
for num in range(2,5):
    f = open("loanstats3"+str(num)+".csv")
    f.next() # skip the header
    f.next() # skip the second header
    for line in f:
         LD.write(line)
    f.close() # not really needed
LD.close()

LD = pd.read_csv("out.csv")

#Selecting column data
intrate = LD['int_rate']
ainc = LD['annual_inc']
homown = LD['home_ownership']

import numpy as np

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(ainc).transpose()
x2 = np.matrix(homown).transpose()

#Creat input matrix
x = np.column_stack([x1,x2])

#Create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#Summary
f.summary.plot()
