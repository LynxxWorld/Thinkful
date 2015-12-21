import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Removing % from 1 row
x = lambda x: round(float(x.rstrip('%')) / 100, 4)

# Removing $ from all rows
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

# Removing 'months' from loan length
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength

# Creating Fico Range
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
loansData['FICO.Range'] = cleanFICORange

import numpy as np
import pandas as pd
import statsmodels.api as sm

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print f.summary()
