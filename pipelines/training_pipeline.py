from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

# enable_cache --> using chached verson of ingest_df. 
# if nothing changes in the code, or data then it will use the step from the prev run
# @pipeline(enable_cache = True)
def train_pipeline(data_path: str) : 
    df = ingest_df(data_path)
    # print('in train_pipeline --> ',type(df))
    X_train, X_test, y_train, y_test = clean_df(df)

    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    print(type(X_train), type(y_train))
    # print(type(train_model()))
    model = train_model(X_train, X_test, y_train, y_test)
    r2_score, rmse = evaluate_model(model, X_test, y_test)

