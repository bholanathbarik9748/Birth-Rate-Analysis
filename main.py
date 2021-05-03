import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# read csv file
data = pd.read_csv("births.csv")
data['decade'] = 10 * (data['year'] // 10)
print(data.head())

# crete plt built-in plotting tools in Pandas to visualize the total number of births by year :
sns.set()
birth = data.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
birth.plot()
plt.ylabel("Total births per year")
plt.show()

# Further data exploration
quartiles = np.percentile(data['births'], [25, 50, 75])
print(f"you quartiles right now:  {quartiles}")
mu = quartiles[0]
mu1 = quartiles[1]
mu2 = quartiles[2]
print(f"Zero index quartiles: {mu}")
print(f"first index quartiles: {mu1}")
print(f"Second index quartiles: {mu2}")

# where the 0.74 comes from the interfertile range of a Gaussian distribution
sign = 0.74 * (quartiles[2] - quartiles[0])
print(f"sigma-clipping: {sign}")

# query() method to filter out rows with births outside these values
data = data.query('(births > @mu - 5 * @sign) & (births < @mu + 5 * @sign)')
data['day'] = data['day'].astype(int)
data.index = pd.to_datetime(10000 * data.year +
                            100 * data.month +
                            data.day, format='%Y%m%d')

data['day_of_week'] = data.index.dayofweek

# plot 2 crete
data.pivot_table('births', index='day_of_week',
                 columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day')
plt.show()

# this month born list
birth_month = data.pivot_table('births', [data.index.month, data.index.day])
print(f"this month head: {birth_month}")

# last plot
fig, ax = plt.subplots(figsize=(12, 4))
birth_month.plot(ax=ax)
plt.show()
