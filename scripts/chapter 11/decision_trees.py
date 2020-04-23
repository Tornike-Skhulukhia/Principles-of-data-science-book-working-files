from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# process data - temp
df = pd.read_csv('data_.csv')

# as we have some missing programs
df.dropna(inplace=True)

feature_cols = ['main_faculty', 'main_program', 'sex', 'birth_year', 'birth_month', 'birth_day']

x = df[feature_cols]
y = df.score

treeclf = DecisionTreeRegressor(max_depth=4)

treeclf.fit(x, y)

# search better ways to visualize...

# tree.plot_tree(treeclf)
# # plt.show()
# plt.savefig('fig.png', orientation='landscape', )

print(pd.DataFrame({'feature':feature_cols, 'importance':treeclf.feature_importances_}))

'''
        feature  importance
0  main_faculty    0.028228
1  main_program    0.019857
2           sex    0.518183
3    birth_year    0.395214
4   birth_month    0.031026
5     birth_day    0.007492
'''