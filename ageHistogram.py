import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy.stats import norm

arr = [26, 23, 22, 31, 24, 34, 21, 22, 21, 28, 27, 21,
       24, 22, 23, 21, 19, 30, 23, 22, 31, 21, 34, 33,
       26, 29, 21, 25, 33, 32, 22, 22, 25, 25, 20]

# the histogram of the data
plt.figure(1)
result = plt.hist(arr, bins = 5)
plt.xlim((min(arr), max(arr)))

# set titles
font = {'fontname':'Times New Roman'}
plt.title("NBA player age (2021 - 2022 season)", **font)
plt.xlabel("Age (year)", **font)
plt.ylabel("Frequency", **font)

# 'best fit' line
mean = np.mean(arr)
sigma = statistics.stdev(arr)
x = np.linspace(min(arr), max(arr), 100)
dx = result[1][1] - result[1][0]
scale = len(arr) * dx
plt.plot(x, norm.pdf(x, mean, sigma) * scale) 

# save and display the figure
plt.savefig("agePlot.png", dpi = 300)
plt.show()

print("mean:", mean)
print("standard deviation:", sigma)