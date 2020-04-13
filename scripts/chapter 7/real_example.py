from import_helpers import pd, plt, dtt
from sklearn import preprocessing


df = pd.read_json('real_data.jl', lines=True)
df = df.set_index('published_at').fillna(0)
df = df[df.index > dtt(2018, 1, 1)].iloc[:-1]

df_scaled = pd.DataFrame(preprocessing.scale(df), columns=['c1_scaled', 'c2_scaled'])

df_scaled.plot(kind='scatter', x='c1_scaled', y='c2_scaled')
plt.show()
