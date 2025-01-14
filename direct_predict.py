import json
import requests
import pandas as pd
import numpy as np

def predict_direct():
    # Sample data (same format as the Streamlit app)
    data = pd.DataFrame(
        {
            "payment_sequential": [0],
            "payment_installments": [0],
            "payment_value": [0.00],
            "price": [0.00],
            "freight_value": [0.00],
            "product_name_lenght": [0.02],
            "product_description_lenght": [-0.02],
            "product_photos_qty": [0.00],
            "product_weight_g": [0.04],
            "product_length_cm": [0.00],
            "product_height_cm": [0.00],
            "product_width_cm": [0.00],
        }
    )
    
    # Convert to the format MLflow expects
    json_data = json.dumps({
        "dataframe_split": {
            "columns": list(data.columns),
            "data": data.values.tolist()
        }
    })
    
    # MLflow serving endpoint
    url = "http://127.0.0.1:8000/invocations"
    
    # Headers required by MLflow
    headers = {
        "Content-Type": "application/json",
    }
    
    try:
        # Make the POST request
        response = requests.post(url, data=json_data, headers=headers)
        
        if response.status_code == 200:
            prediction = response.json()
            print(f"Prediction: {prediction}")
            return prediction
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    predict_direct()
