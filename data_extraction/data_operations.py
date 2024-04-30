"""
This module uses the functions from the tutorial
of the course Recommender Systems.
"""

import pandas as pd


dir_train = 'ml-100k'

# Generamos los títulos de las columnas del archivo items.

item_cols = ['itemid', 'title', 'release_date', 'video_release_date', \
             'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation', \
             'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', \
             'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', \
             'Thriller', 'War', 'Western']

def combine_genres(row):
    genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama',
              'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War',
              'Western']
    
    return '|'.join([col for col, val in row.items() if val == 1 and col in genres])

def load_data():
    df_items = pd.read_csv(f'{dir_train}/u.item', sep='|',index_col=0,
                           names = item_cols, header=None, encoding='latin-1')
    
    df_items = df_items.reset_index()
    df_items['genres'] = df_items.apply(combine_genres, axis=1)
    genres = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama',
              'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War',
              'Western']
    df_items = df_items.drop(genres, axis=1)
    
    return df_items