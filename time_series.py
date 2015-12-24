import pandas as pd
import numpy as np
import statsmodels

LD = pd.read_csv('out.csv', header = 0, low_memory = False)

# converts string to datetime object in pandas:
LD['issue_d_format'] = pd.to_datetime(LD['issue_d'])
LDts = LD.set_index('issue_d_format')
year_month_summary = LDts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

loan_count_summary.plot()

statsmodels.api.graphics.tsa.plot_acf(loan_count_summary)
statsmodels.api.graphics.tsa.plot_pacf(loan_count_summary)
