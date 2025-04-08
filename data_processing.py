from pandas import DataFrame

def load_data(file_path: str) -> DataFrame:
    """
    Loads data from a specified file path.
    Called by main.py to get the raw data.
    """
    # Simulated data loading
    return DataFrame()

def preprocess_data(data: DataFrame) -> DataFrame:
    """
    Cleans and preprocesses the data for model training.
    Interacts with load_data() to receive raw data and return processed data to main.py.
    """
    # Simulated data preprocessing
    return data