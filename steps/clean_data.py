import logging 
import pandas as pd 
from zenml import step 

from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessStrategy

@step 
def clean_df(df: pd.DataFrame) : 
    try : 
        preprocess_strategy = DataPreProcessStrategy()
        data_cleaning = DataCleaning(df, preprocess_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, divide_strategy)
        # print('in clean_df --> steps --> ', data_cleaning.handle_data())
        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info("data cleaning completed")
        # print(X_train, X_test, y_train, y_test)
        return X_train, X_test, y_train, y_test

    except Exception as e : 
        logging.error("error in data cleaning {}".format(e))
        raise e 