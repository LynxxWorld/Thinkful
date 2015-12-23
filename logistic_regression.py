from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

# Load the reduced version of the Lending Club Dataset
LD = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

#Clean Data
LD['Interest.Rate'] = LD['Interest.Rate'].map(lambda x: float(x.rstrip('%')))
LD['Loan.Length'] = LD['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
LD['FICO.Range'] = LD['FICO.Range'].map(lambda x: x.split('-'))

#Insert IR_TF Column with lambda function for <12%
LD.insert(3,'IR_TF', 0) # How to input a lambda function into the third argument?
LD['IR_TF'] = LD['Interest.Rate'].map(lambda x: 0 if x < 12 else 1)

#Insert intecept column
LD.insert(15,'Intercept',1.0)

#List Columns
ind_vars = list(LD.columns.values)
ind_vars

#Logit Function -- not working
#logit = sm.Logit(LD['IR_TF'], LD[ind_vars]) -- #doesn't seem to work
#result = logit.fit()
#coeff = result.params
#print (coeff)

#Logistic Function
def logistic_function(intercept, FICO_Score, Loan_Amount):
    p = 1/(1 + np.exp(intercept + 0.087423 * FICO_Score - 0.000174 * Loan_Amount))
    print p

logistic_function(-12,720,10000)

#Plot -- Doesn't seem correct / Not working
y = np.arange(550,950,0.5)
p = 1/(1 + np.exp(-12 + 0.087423*y - 0.000174*10000))
plt.plot(y,p)
plt.show()
