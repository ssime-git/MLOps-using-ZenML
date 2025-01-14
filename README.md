# MLOps Project using ZenML

This project demonstrates an end-to-end MLOps pipeline using ZenML for customer satisfaction prediction.

## Project Structure
```
.
├── data/                  # Dataset directory
├── notebooks/            # Jupyter notebooks
├── pipelines/           # ZenML pipeline definitions
├── src/                 # Source code
├── steps/               # Pipeline steps
├── docs/               # Documentation and diagrams
└── app.py              # Streamlit application
```

## Architecture

![Architecture Diagram](docs/architecture.png)

The project follows a modular architecture with several key components:

1. **Data Pipeline**: Handles data ingestion and preprocessing
2. **Training Pipeline**: Manages model training and evaluation
3. **Deployment Pipeline**: Controls model deployment and serving
4. **Monitoring**: Uses MLflow and ZenML for tracking and monitoring

For a detailed view, see the [architecture diagram](docs/architecture.md).

## Overview
This project implements an end-to-end MLOps pipeline using ZenML for customer satisfaction prediction. The pipeline includes:
- Data ingestion and cleaning
- Model training (Linear Regression)
- Model evaluation
- Automated deployment with MLflow
- Prediction service
- Web interface with Streamlit

## Monitoring and Visualization

### 1. ZenML Dashboard
```bash
# Start the ZenML UI server
zenml up

# Access the dashboard at http://127.0.0.1:8237
# Default credentials:
# Username: default
# Password: (no password required)
```

The ZenML Dashboard provides:
- Pipeline execution history
- Step-by-step visualization
- Stack configuration
- Service status
- Artifact tracking

### 2. MLflow UI
```bash
mlflow ui --backend-store-uri 'file:/Users/seb/Library/Application Support/zenml/local_stores/<your-store-id>/mlruns' --host 0.0.0.0 --port 5001
```

The MLflow UI offers:
- Experiment tracking
- Parameter logging
- Metric visualization
- Model registry
- Run comparison

### 3. Streamlit Interface
```bash
streamlit run app.py
```

Provides:
- Interactive model predictions
- Input parameter adjustment
- Results visualization

## Prerequisites
- Python 3.12+
- pip or conda for package management

## Setup Instructions

1. Clone the repository and create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Install dependencies:
```bash
pip install -e .
# Or alternatively
pip install -r requirements.txt
```

3. Initialize ZenML:
```bash
zenml init
```

4. Set up MLflow integration:
```bash
# Install MLflow integration
zenml integration install mlflow

# Register the MLflow model deployer
zenml model-deployer register mlflow_deployer --flavor=mlflow

# Register the MLflow experiment tracker
zenml experiment-tracker register mlflow_tracker --flavor=mlflow

# Update existing stack with the experiment tracker (if you already have a stack)
zenml stack update mlflow_stack -e mlflow_tracker

# Or create a new stack with MLflow components
zenml stack register mlflow_stack \
    -a default \
    -o default \
    -d mlflow_deployer \
    -e mlflow_tracker

# Set it as the active stack
zenml stack set mlflow_stack
```

## Running the Project

1. Train and Deploy the Model:
```bash
# Deploy the model with a specified minimum accuracy threshold
# Note: The current model achieves ~1.8% accuracy, so we set a low threshold for demonstration
python run_deployment.py --config deploy --min-accuracy 0.01

# After deployment is successful, you should see a message indicating
# the model is running at http://127.0.0.1:8000/invocations
```

2. View MLflow Experiment Results:
```bash
mlflow ui --backend-store-uri 'file:/Users/seb/Library/Application Support/zenml/local_stores/<your-store-id>/mlruns' --host 0.0.0.0 --port 5001
```
This will make the MLflow UI accessible at http://localhost:5001

3. Start the Prediction Service:
```bash
python run_deployment.py --config predict
```

4. Start the Streamlit application:
```bash
streamlit run app.py
```

## Model Performance Metrics
The current model achieves the following metrics:
- MSE: 1.864
- RMSE: 1.365
- R² Score: 0.018 (1.8% accuracy)

Note: The current model performance is quite low. This is intentional for demonstration purposes, but in a production environment, you would want to improve the model's performance before deployment.

## Pipeline Components

### 1. Data Processing
- Data ingestion from CSV files
- Cleaning and preprocessing of customer data
- Feature engineering and preparation

### 2. Model Training
- Uses scikit-learn's Linear Regression
- Automated training pipeline with MLflow tracking
- Model metrics and parameters are logged automatically

### 3. Deployment System
- Automated model deployment using MLflow
- Deployment trigger based on model accuracy
- REST API endpoint for predictions
- Model serving at http://127.0.0.1:8000/invocations

### 4. Monitoring
- MLflow experiment tracking
- Model performance monitoring
- Deployment status tracking

## Troubleshooting

1. Verify your ZenML stack:
```bash
zenml stack list
zenml stack describe
```

2. Check MLflow integration:
```bash
zenml integration list
zenml model-deployer list
zenml experiment-tracker list
```

3. Common issues:
   - If MLflow components are not found: Re-run the stack registration
   - If imports fail: Ensure you're in the virtual environment
   - If model deployment fails: Check MLflow UI for detailed logs
   - If prediction service isn't running: Ensure deployment succeeded and accuracy threshold was met

4. Managing the Deployment:
   - View running services: `zenml model-deployer models list`
   - Stop a service: `zenml model-deployer models delete <service-uuid>`
   - Check service status: `zenml model-deployer models get <service-uuid>`

## Cleanup and Reset

To stop all services and reset the environment:

1. Stop MLflow Deployment:
```bash
# List all deployed models
zenml model-deployer models list

# Delete deployed models (replace UUID with actual ID)
zenml model-deployer models delete <UUID>
```

2. Stop ZenML UI:
```bash
zenml down
```

3. Clean MLflow and ZenML:
```bash
# Clean MLflow runs
rm -rf mlruns/

# Clean ZenML local store
rm -rf ~/Library/Application\ Support/zenml/local_stores/*

# Reset ZenML stack
zenml stack delete mlflow_stack
zenml stack set default
```

4. Clean Python Cache:
```bash
# Remove all __pycache__ directories
find . -type d -name "__pycache__" -exec rm -r {} +
```

5. Complete ZenML Reset (Optional):
```bash
zenml clean
```

To start fresh after cleanup:
```bash
# Create and set new stack
zenml stack register mlflow_stack -a default -o default -d mlflow_deployer -e mlflow_tracker
zenml stack set mlflow_stack

# Run deployment
python run_deployment.py --config deploy --min-accuracy 0.01
```

## Contributing

Feel free to open issues or submit pull requests for any improvements.