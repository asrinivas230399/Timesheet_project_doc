# model.py

from pandas import DataFrame

class Model:
    pass

def train_model(data: DataFrame) -> Model:
    """
    Trains a machine learning model using the processed data.
    Called by main.py after data preprocessing.
    """
    pass

def evaluate_model(model: Model, test_data: DataFrame) -> dict:
    """
    Evaluates the trained model on test data.
    Returns evaluation metrics to main.py.
    """
    pass