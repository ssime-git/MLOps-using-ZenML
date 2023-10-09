## MLOPs using ZenML

NGROK_TOKEN is saved in the config.py file. to run the `pipeline.ipynb` login to ngrok and create your account and save your token inside the `config.py` file inside notebooks. 

```py
"""
|- notebooks 
|   |- config.py
|   |- pipeline.ipynb
|
"""
NGROK_TOKEN = "your_unique_token"
```
```
<!-- install mlflow -->
zenml integration install mlflow -y
```