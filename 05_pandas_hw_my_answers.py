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
movies.content_rating.value_counts().plot(kind='bar')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP


# convert the following content ratings to "NC-17": X, TV-MA


# count the number of missing values in each column
movies[movies.star_rating.isnull()].shape[0]
movies[movies.title.isnull()].shape[0]
movies[movies.content_rating.isnull()].shape[0]
movies[movies.genre.isnull()].shape[0]
movies[movies.duration.isnull()].shape[0]
movies[movies.actors_list.isnull()].shape[0]

# if there are missing values: examine them, then fill them in with "reasonable" values


# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours

# use a visualization to detect whether there is a relationship between duration and star rating


# calculate the average duration for each genre


'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration


# determine the top rated movie (by star rating) for each genre


# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates


# calculate the average star rating for each genre, but only include genres with at least 10 movies



'''
BONUS
'''

# Figure out something "interesting" using the actors data!
