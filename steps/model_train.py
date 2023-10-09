import logging 
import pandas as pd 
from zenml import step 

# from src.model_dev import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.base import RegressorMixin
from .config import ModelNameConfig

import mlflow 
from zenml.client import Client 

experiment_tracker = Client().ative_stack.experiment_tracker

@step(experiment_tracker = experiment_tracker.name)
def train_model(
    X_train : pd.DataFrame,
    X_test : pd.DataFrame,
    y_train : pd.Series,
    y_test : pd.Series
) : 

    try : 
        model = None 
        # if config.model_name == "LinearRegression" : 
        mlflow.sklearn.autolog()
        model = LinearRegression()
        trained_model = model.fit(X_train, y_train)
        print('train model-->', type(trained_model))
        return trained_model 

        # else : 
        #     raise ValueError(f'Model {config.model_name} not supported')
    except Exception as e: 
        logging.error("error in training model steps : {}".format(e))
        raise e 