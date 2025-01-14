import logging 
import pandas as pd 
from zenml import step 

from typing import Tuple
from src.evaluation import MSE, RMSE, R2
from sklearn.base import RegressorMixin
from typing_extensions import Annotated 
import mlflow  
from zenml.client import Client 

# Get experiment tracker if available, otherwise None
experiment_tracker = Client().active_stack.experiment_tracker

# Only use experiment tracker if it exists
@step(experiment_tracker=experiment_tracker.name if experiment_tracker else None)
def evaluate_model(
    model: RegressorMixin,
    X_test: pd.DataFrame,
    y_test: pd.Series
) -> Tuple[
    Annotated[float, "r2_score"],
    Annotated[float, "rmse"]
]: 
    try:
        prediction = model.predict(X_test)
        
        mse_class = MSE()
        mse = mse_class.calculate_score(y_test, prediction)
        mlflow.log_metric("mse", mse)
        
        rmse_class = RMSE()
        rmse = rmse_class.calculate_score(y_test, prediction)
        mlflow.log_metric("rmse", rmse)
        
        r2_class = R2()
        r2_score = r2_class.calculate_score(y_test, prediction)
        mlflow.log_metric("r2_score", r2_score)
        
        return r2_score, rmse

    except Exception as e:
        logging.error("Error in evaluating model: {}".format(e))
        raise e