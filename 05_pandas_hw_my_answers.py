'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_table('data\imdb_1000.csv',sep=',')

# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration')

# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist',bins=10)

# use a box plot to display that same data
movies.duration.plot(kind='box')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title='Count Per Rating',fontsize=8)
plt.xlabel('Rating')
plt.ylabel('Count')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace(['NOT RATED','APPROVED','PASSED','GP'],'UNRATED',True) #inplace=True so change the actual data in movies

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X','TV-MA'],'NC-17',True)

# count the number of missing values in each column
movies[movies.star_rating.isnull()].shape[0]
movies[movies.title.isnull()].shape[0]
movies[movies.content_rating.isnull()].shape[0]
movies[movies.genre.isnull()].shape[0]
movies[movies.duration.isnull()].shape[0]
movies[movies.actors_list.isnull()].shape[0]

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()].title #yields 3 movies with indices: 187, 649, 936
movies.loc[187,'content_rating']='PG-13' #Butch Cassidy and the Sundance Kid
movies.loc[649,'content_rating']='PG' #Where Eagles Dare
movies.loc[936,'content_rating']='PG-13' #True Grit

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration>=120].star_rating.mean() #7.948898678414082 => longer movies have higher averate star rating
movies[movies.duration<120].star_rating.mean() #7.838666666666657 => shorter movies have lower average star rating

# use a visualization to detect whether there is a relationship between duration and star rating
movies['dur_bin']=(movies.duration//20)*20 #add new column that groups duration into 20 minute bins
movies.groupby('dur_bin').star_rating.mean().plot(title='Average Star Rating vs. Duration') #line chart showing movies with duration between 200 and 219 have highest rating

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.boxplot(column='duration', by='content_rating') #PG-13 has the longest mean duration, G the shortest

# determine the top rated movie (by star rating) for each genre
s=movies.groupby('genre').star_rating.max() #series of top rating per genre
for i in range(len(s)): #for each genre...
    movies[(movies.genre==s.index[i]) & (movies.star_rating==s[i])][['genre','star_rating','title']] #...select the movie(s) w/ top rating in that genre
                                                                                                     #     and show columns genre, star rating, title

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies.title.value_counts() #
                            #
movies[(movies.title=='The Girl with the Dragon Tattoo')|(movies.title=='Dracula')|(movies.title=='Les Miserables')|(movies.title=='True Grit')].sort('title')

# calculate the average star rating for each genre, but only include genres with at least 10 movies
df=movies.groupby('genre').star_rating.agg(['count','mean']) #get count, mean star rating of each genre
df[df['count']>9]['mean']                                    #show the mean star rating for each genre (can't use dot notation because df has same-named functions)

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
This code...

lActors = [] #every citation of an actor
for al in movies.actors_list: #iterate thru the actors_list column (each item is a list in the form of a string)
    for a in eval(al): #convert the string representation of the list into a real list and iterate thru it
        lActors.append(a) #add each citation of an actor to the actors list

actor_counts = Counter(lActors) #get counts of each actor cited 
for actor, count in actor_counts.most_common(50): #print the actors most commonly cited in descending order
    print actor, count

...shows that Robert De Niro is cited the most (18) 


