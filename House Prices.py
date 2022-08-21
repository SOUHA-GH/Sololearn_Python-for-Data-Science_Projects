#The program calculates and outputs the percentage of houses in the given array that are within one standard deviation from the mean.
import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
m=np.mean(data)
stdvar = np.std(data)
l,h = m-stdvar,m+stdvar
num = len([hp for hp in data if l < hp < h])
print((num/len(data))*100)
