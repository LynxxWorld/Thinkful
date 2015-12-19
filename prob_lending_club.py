import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

import matplotlib.pyplot as plt
import pandas as pd

loansData.boxplot(column='Amount.Requested')

plt.show()
plt.savefig("lending_boxplot.png")

loansData.hist(column='Amount.Requested')
plt.savefig("lending_histo.png")

import scipy.stats as stats

graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()
plt.savefig("lending_QQ.png")
