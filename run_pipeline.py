from pipelines.training_pipeline import train_pipeline
import logging 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler('app.log')
    ]
)

if __name__ == '__main__' : 
    train_pipeline(data_path = 'data/olist_customers_dataset.csv')