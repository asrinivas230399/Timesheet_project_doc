from data_processing import load_data, preprocess_data
from model import train_model, evaluate_model
from utils import load_config, log
from security import authenticate_user, log_audit_event


def main():
    """
    Entry point of the application.
    Calls functions from data_processing.py to load and preprocess data.
    Utilizes model.py to train and evaluate the model.
    Interacts with utils.py for any utility functions needed.
    """
    config = load_config('config.yaml')
    log('Configuration loaded.')
    
    raw_data = load_data(config['data_path'])
    log('Data loaded.')
    
    processed_data = preprocess_data(raw_data)
    log('Data preprocessed.')
    
    model = train_model(processed_data)
    log('Model trained.')
    
    evaluation_metrics = evaluate_model(model, processed_data)
    log(f'Model evaluated with metrics: {evaluation_metrics}')

    # Example of user authentication and audit logging
    if authenticate_user('admin', 'password'):
        log('User authenticated successfully.')
        log_audit_event('User admin logged in successfully.')
    else:
        log('Authentication failed.')
        log_audit_event('Failed login attempt for user admin.')


if __name__ == "__main__":
    main()
