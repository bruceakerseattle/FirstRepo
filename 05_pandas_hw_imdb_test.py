# 05_pandas_hw_imdb_test.py
# Developed by Bruce Aker - 11/28/15

# Determine most frequently listed actor in the IMDB 1000 movies data file

import pandas as pd
from collections import Counter

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_table('data\imdb_1000.csv',sep=',')

lActors = [] #every citation of an actor
for al in movies.actors_list: #iterate thru the actors_list column (each item is a list in the form of a string)
    for a in eval(al): #convert the string representation of the list into a real list and iterate thru it
        lActors.append(a) #add each citation of an actor to the actors list
actor_counts = Counter(lActors) #get counts of each actor cited 
for actor, count in actor_counts.most_common(70): #print the actors most commonly cited in descending order
    print actor, count



