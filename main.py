import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

fandango = pd.read_csv("fandango_scrape.csv")

# print(fandango.head())
# print(fandango.info())
# print(fandango.describe())


# plt.figure(figsize=(12, 5))
# sns.scatterplot(data=fandango, x='RATING', y='VOTES')         #graph raiting vs votes
# plt.show()

fandango['YEAR'] = fandango['FILM'].apply(
    lambda title: title.split('(')[-1][:-1])  # creating year column from film
# print(fandango['YEAR'].value_counts())

# plt.figure(figsize=(12, 5))
# sns.countplot(data=fandango, x='YEAR')            #graph films in year
# plt.show()

# print(fandango.nlargest(10, 'VOTES'))         #top ten films by votes

# print(fandango[fandango['VOTES'] == 0].value_counts)            #films without rating

f_with_votes = fandango[fandango['VOTES'] > 0]  # only films with votes

# plt.figure(figsize=(12, 5))
# sns.kdeplot(data=f_with_votes,x='RATING',clip=[0,5],fill=True,label='True Rating')
# sns.kdeplot(data=f_with_votes,x='STARS',clip=[0,5],fill=True,label='Stars Displayed')           #graph raiting vs stars
# plt.show()

f_with_votes['STARS_DIFF'] = f_with_votes['STARS'] - f_with_votes['RATING']
f_with_votes['STARS_DIFF'] = f_with_votes['STARS_DIFF'].round(2)
print(f_with_votes.head(10))

plt.figure(figsize=(12, 5))
# graph difference between stars and votes
sns.countplot(data=f_with_votes, x='STARS_DIFF', palette='magma')
plt.show()
