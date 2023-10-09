from pipelines.training_pipeline import train_pipeline
import logging 

if __name__ == '__main__' : 
    train_pipeline(data_path = 'data/olist_customers_dataset.csv')