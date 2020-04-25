import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(
            'https://raw.githubusercontent.com/PacktPublishing/Principles-of-Data-Science-Second-Edition/master/Chapter11/beer.txt',
            sep=' ')
x = df.drop('name', axis=1)

km = KMeans(n_clusters=3)

km.fit(x)

df['cluster'] = km.labels_

centers = df.groupby('cluster').mean()
colors = np.array(['red', 'green', 'blue', 'yellow'])

plt.scatter(df.calories, df.alcohol, c=colors[list(df.cluster)], s=50)
plt.scatter(centers.calories, centers.alcohol, c='k', s=300, marker='+')

plt.xlabel('calories')
plt.ylabel('alcohol')

plt.show()
