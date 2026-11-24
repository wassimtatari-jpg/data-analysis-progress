import pandas as pd

movies = pd.DataFrame({
    'title': ['Avatar', 'Titanic', 'Jaws', 'Gladiator'],
    'year': [2009, 1997, 1975, 2000]
}, index=pd.Index([1, 2, 3, 4], name='id'))

ratings = pd.DataFrame({
    'rating': [7.9, 7.8, 8.1],
    'votes': [1500, 2000, 1200]
}, index=pd.Index([1, 3, 4], name='movie_id'))

my_table=movies.merge(ratings,how="inner",left_on='id',right_index=True)
print(my_table)
my_table=movies.merge(ratings,how="left",left_index=True,right_index=True)
print(my_table)