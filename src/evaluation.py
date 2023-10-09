import logging 
from abc import ABC, abstractmethod
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np 

class Evaluation(ABC) :
    @abstractmethod
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) : 
        pass 

class MSE(Evaluation) : 
    """
    evaluation strategy that uses MSE 
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) : 
        try : 
            logging.info("calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info(f"MSE : {mse}")
            return mse 

        except Exception as e: 
            logging.error("error in calculaing mse : {}".format(e))
            raise e 

class R2(Evaluation) : 
    """
    evaluation strategy that uses MSE 
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) : 
        try : 
            logging.info("calculating MSE")
            r2 = r2_score(y_true, y_pred)
            logging.info(f"r2 score : {r2}")
            return r2 

        except Exception as e: 
            logging.error("error in calculaing r2 score : {}".format(e))
            raise e 

class RMSE(Evaluation) : 
    """
    evaluation strategy that uses MSE 
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) : 
        try : 
            logging.info("calculating MSE")
            rmse = mean_squared_error(y_true, y_pred, squared = False)
            logging.info(f"RMSE : {rmse}")
            return rmse 

        except Exception as e: 
            logging.error("error in calculaing RMSE : {}".format(e))
            raise e 