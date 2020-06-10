from sklearn.externals import joblib
import pandas as pd


def predict(email):
    """
    input email pandas series, return prediction csv file
    :param email: pandas.series
    :return: gender prediction csv file
    """
    filename = 'test_LR1.sav'
    loaded_model = joblib.load(filename)
    pred = loaded_model.predict(email)
    pd.DataFrame(pred).to_csv('predict.csv')
    return pred




