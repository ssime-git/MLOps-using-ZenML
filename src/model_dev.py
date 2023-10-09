import logging 
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression

class Model(ABC) : 
    """
    abstract class for all models
    """
    @abstractmethod 
    def train(self, X_train, y_train): 
        pass 


class LinearRegression(Model) : 
    def train(self, X_train, y_train, **kwargs) : 
        try :
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return reg 
        except Exception as e: 
            logging.error("error in training model src : {}".format(e))
            raise e 