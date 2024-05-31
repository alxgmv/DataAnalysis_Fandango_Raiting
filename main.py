import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

fandango = pd.read_csv("fandango_scrape.csv")

plt.figure(figsize=(12, 5))
sns.scatterplot(data=fandango, x='RATING', y='VOTES')         # graph raiting vs votes
plt.show()

fandango['YEAR'] = fandango['FILM'].apply(
    lambda title: title.split('(')[-1][:-1])            # creating year column from film
# print(fandango['YEAR'].value_counts())

# plt.figure(figsize=(12, 5))
# sns.countplot(data=fandango, x='YEAR')            # graph films in year
# plt.show()

# print(fandango.nlargest(10, 'VOTES'))         # top ten films by votes

# print(fandango[fandango['VOTES'] == 0].value_counts)            # films without rating

# f_with_votes = fandango[fandango['VOTES'] > 0]            # only films with votes

# plt.figure(figsize=(12, 5))
# sns.kdeplot(data=f_with_votes,x='RATING',clip=[0,5],fill=True,label='True Rating')
# sns.kdeplot(data=f_with_votes,x='STARS',clip=[0,5],fill=True,label='Stars Displayed')           # graph raiting vs stars
# plt.show()

# f_with_votes['STARS_DIFF'] = f_with_votes['STARS'] - f_with_votes['RATING']
# f_with_votes['STARS_DIFF'] = f_with_votes['STARS_DIFF'].round(2)            # difference between stars and votes
# print(f_with_votes.head(10))

# plt.figure(figsize=(12, 5))
# sns.countplot(data=f_with_votes, x='STARS_DIFF', palette='magma')           # graph difference between stars and votes
# plt.show()

all_sites = pd.read_csv("all_sites_scores.csv")

# print(all_sites.head())

# plt.figure(figsize=(12, 5))
# sns.scatterplot(data=all_sites, x='RottenTomatoes', y='RottenTomatoes_User')            # graph rotten tomatoes vs rotten tomatoes users
# plt.xlim(0,100)
# plt.ylim(0,100)         
# plt.show()

all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']           # difference between rotten tomatoes vs rotten tomatoes users
all_sites['Rotten_Diff'] = all_sites['Rotten_Diff'].round(2)      
rotten_diff_mean = round(abs(all_sites['Rotten_Diff']).mean(), 2)
# print(rotten_diff_mean)

# plt.figure(figsize=(12, 5))
# sns.histplot(data=all_sites, x= 'Rotten_Diff', kde=True, bins=25)          # graph difference between rotten tomatoes vs rotten tomatoes users
# plt.xlim(-70, 50)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(12, 5))
# sns.histplot(x=all_sites['Rotten_diff'].apply(abs),bins=25,kde=True)        # graph abs difference between rotten tomatoes vs rotten tomatoes users
# plt.xlim(0, 80)
# plt.tight_layout()
# plt.show()

# print(all_sites.nsmallest(5,'Rotten_Diff')[['FILM','Rotten_Diff']])         # biggest difference between critic raiting and user rating (lowest critic highest user)
# print(all_sites.nlargest(5,'Rotten_Diff')[['FILM','Rotten_Diff']])          # biggest difference between critic raiting and user rating (highest critic lowest user)


# plt.figure(figsize=(12, 5))
# sns.scatterplot(data=all_sites, x='Metacritic', y='Metacritic_User')        # graph metacritic vs metacritic users
# plt.xlim(0,100)
# plt.ylim(0,10)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(12, 5))
# sns.scatterplot(data=all_sites, x='Metacritic_user_vote_count', y='IMDB_user_vote_count')        # graph metacritic user votes vs IMDB  user votes
# # plt.xlim(0,100)
# # plt.ylim(0,10)
# plt.tight_layout()
# plt.show()

# highest_IMDB = all_sites.nlargest(1, 'IMDB_user_vote_count')            # film with highest IMDB votes 
# print(highest_IMDB)

# highest_Metacritic = all_sites.nlargest(1, 'Metacritic_user_vote_count')            # film with highest Metacritic votes
# print(highest_Metacritic)

df = pd.merge(fandango,all_sites,on='FILM',how='inner')         # merging fandango table woth all_sites table
# print(df)

df['Metacritic_norm'] = round(df['Metacritic']/20, 1)
df['Metacritic_U_norm'] = round(df['Metacritic_User']/2, 1)
df['RottenTomatoes_norm'] = round(df['RottenTomatoes']/20, 1)         # normalizing raitings of different sites to the scale 0..5
df['RottenTomatoes_u_norm'] = round(df['RottenTomatoes_User']/20, 1) 
df['IMDB_norm'] = round(df['IMDB']/2, 1)


# print(df[['FILM', 'RATING', 'Metacritic_norm', 'RottenTomatoes_norm', 'IMDB_norm']].head(5))

norm_scores = df[['STARS','RATING', 'Metacritic_norm', 'Metacritic_U_norm', 'RottenTomatoes_norm', 'RottenTomatoes_u_norm', 'IMDB_norm', 'FILM']]     # creating new dataframe with all ratings

# print(norm_scores)

def move_legend(ax, new_loc, **kws):
    old_legend = ax.legend_
    handles = old_legend.legend_handles
    labels = [t.get_text() for t in old_legend.get_texts()]             # creating custom legend and moving it to the top right corner
    title = old_legend.get_title().get_text()
    ax.legend(handles, labels, loc=new_loc, title=title, **kws)  


# fig, ax = plt.subplots(figsize=(12,4),dpi=100)
# sns.kdeplot(data=norm_scores,clip=[0,5], palette='Set1', ax=ax, fill=True)            # graph with all rating together
# move_legend(ax, "upper left")
# plt.show()

# fig, ax = plt.subplots(figsize=(12,4),dpi=100)
# sns.kdeplot(data=norm_scores[['RottenTomatoes_norm', 'STARS']], clip=[0,5], palette='Set1', ax=ax, fill=True)         # graph Rotten tomatoes critic vs Stars from Fandango

# move_legend(ax, "upper left")
# plt.show()

# plt.figure(figsize=(12, 5))
# sns.histplot(data=norm_scores, bins=45)           # histogram with all ratings
# plt.show()

# sns.clustermap(norm_scores,cmap='magma',col_cluster=False)          # cluster graph with all ratings
# plt.show()

lowest_rt = norm_scores.nsmallest(10, 'RottenTomatoes_norm')            # film with lowest Rotten Tomatoes normalized rating
# print(lowest_rt)

# fig, ax = plt.subplots(figsize=(12,4),dpi=100)
# sns.kdeplot(data=lowest_rt, clip=[0,5], palette='Set1', ax=ax, fill=True)            # graph lowest Rotten Tomatoes normalized rating vs others
# move_legend(ax, "upper right")
# plt.show()

