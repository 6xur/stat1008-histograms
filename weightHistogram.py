import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy.stats import norm

arr = [95, 91, 112, 99, 92, 99, 85, 95, 87, 88, 108, 97,
       95, 95, 112, 122, 88, 97, 86, 106, 114, 78, 117, 83,
       108, 93, 79, 102, 108, 81, 104, 94, 103, 97, 99]

# the histogram of the data
plt.figure(1)
result = plt.hist(arr, bins = 6)
plt.xlim((min(arr), max(arr)))

# set titles
font = {'fontname':'Times New Roman'}
plt.title("NBA player weight (2021 - 2022 season)", **font)
plt.xlabel("Weight (kg)", **font)
plt.ylabel("Frequency", **font)

# 'best fit' line
mean = np.mean(arr)
sigma = statistics.stdev(arr)
x = np.linspace(min(arr), max(arr), 100)
dx = result[1][1] - result[1][0]
scale = len(arr) * dx
plt.plot(x, norm.pdf(x, mean, sigma) * scale) 

# save and display the figure
plt.savefig("weightPlot.png", dpi = 1200)
plt.show()

print("mean:", mean)
print("standard deviation:", sigma)