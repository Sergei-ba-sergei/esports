import pandas as pd

def get_some_amateurs():
    all_names = pd.read_csv('./src/clean_data/player_names.csv')
    return list(all_names.iloc[:,0].sample(10).values)

