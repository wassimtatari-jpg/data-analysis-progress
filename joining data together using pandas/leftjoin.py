
import pandas as pd
import numpy as np

# Movies DataFrame
movies = pd.DataFrame({
    'movie_id': [101, 102, 103, 104, 105],
    'title': ['The Journey', 'Dark Night', 'Blue World',
              'Last Hope', 'The Dream'],
    'genre_id': [1, 2, 1, 3, 2],
    'rating': [7.5, 8.2, 6.9, 7.8, 8.5]
})

# Financials DataFrame
financials = pd.DataFrame({
    'movie_id': [101, 102, 103, 104],
    'budget': [2000000, 5000000, np.nan, 1500000],
    'revenue': [8000000, 12000000, 3000000, 6000000],
    'rating': [7.4, 8.1, 7.0, 7.9]
})

# Genres DataFrame
genres = pd.DataFrame({
    'genre_id': [1, 2, 3],
    'genre_name': ['Adventure', 'Drama', 'Action']
})
movies_full=movies.merge(financials,on="movie_id",how='left')\
                  .merge(genres,on='genre_id',suffixes=("_mov","_fina"))
print(movies_full)
check_null=movies_full.loc[movies_full['budget'].isnull()]
print(check_null)