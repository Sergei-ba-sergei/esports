import xgboost
import pickle
import pandas as pd

# need to import model
# need to import data

def get_player_prediction(name: str):
    loaded_model = pickle.load(open('./src/models/xgb_classifier.pkl', 'rb'))
    data = pd.read_csv('./src/clean_data/clean_data.csv')
    to_predict = data.loc[data['name'] == name]
    X = to_predict.iloc[:, :-1].drop(columns=['pro_flag', 'Unnamed: 0'])

    predictions = loaded_model.predict(X)
    result = predictions.mean()

    if result >= 0.5:
        result_string = 'We think this person has pro potential!'
    else:
        result_string = 'Ah, this player needs to keep training'

    return result_string



# need to create function that:
# takes a player name,
# filters data by it
# puts through model
# gets results & averages, and converts answer to a string depending on number of yes/no vals

# returns just the string