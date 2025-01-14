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

```sh
<!-- install mlflow -->
zenml integration install mlflow -y
```

# mes notes

## Installation de uv

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init
uv venv
source .venv/bin/activate
uv add pip "zenml[server]" pyngrok
zenml integration install sklearn -y
```