import logging 
import pandas as pd 
from zenml import step 

@step 
def trian_model(df: pd.DataFrame) -> pd.DataFrame : 
    pass 