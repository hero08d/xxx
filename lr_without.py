import numpy as np
import matplotlib.pyplot as plt

# sample data
x = np.array([0,1,2,3,4,5])
y = np.array([1,2,3,5,7,8])

# calculate coefficients
n = len(x)
mx = np.mean(x)
my = np.mean(y)

b1 = (np.sum(x*y) - n*mx*my) / (np.sum(x*x) - n*mx*mx)
b0 = my - b1*mx

print("Slope:", b1)
print("Intercept:", b0)

# prediction
ypred = b0 + b1*x

# plot
plt.scatter(x, y)
plt.plot(x, ypred)
plt.show()
