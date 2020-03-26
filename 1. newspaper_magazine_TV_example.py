import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

data = pd.read_csv(
    'https://raw.githubusercontent.com/PacktPublishing/Principles-of-Data-Science-Second-Edition/master/Chapter01/Advertising.csv',
    index_col=0)

# print(data.head())

# see which has the strongest correlation
# TV           0.782224
# radio        0.576223
# newspaper    0.228299
print(data.corr().loc['sales'].sort_values(ascending=False))

# visualize with seaborn
sns.pairplot(data,
             x_vars=['TV', 'radio', 'newspaper'],
             y_vars='sales',
             height=4.5,
             aspect=0.7)

plt.show()