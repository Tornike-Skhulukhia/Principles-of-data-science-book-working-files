import pandas as pd

drinks = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/principles_of_data_science/master/data/chapter_2/drinks.csv')

print(drinks.head())

print(drinks.describe())