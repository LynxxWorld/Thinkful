import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
box_plot = plt.boxplot(x)
plt.show()
plt.savefig("boxplot.png")

hist_plot = plt.hist(x, histtype='bar')
plt.show()
plt.savefig("histo.png")

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

test_data = np.random.normal(size=1000)   
normal_graph = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()
plt.savefig("normal.png") #this will generate the first graph

test_data2 = np.random.uniform(size=1000)   
uniform_graph = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()
plt.savefig("uniform.png") #this will generate the second graph
