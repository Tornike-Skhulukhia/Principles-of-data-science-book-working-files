
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

means = []

for i in range(1, 10_001):
    rand_arr = np.random.randint(1, 10, i)
    mean = np.mean(rand_arr)
    means.append(mean) 

df = pd.DataFrame({'means': means})
df.plot()
plt.show()
