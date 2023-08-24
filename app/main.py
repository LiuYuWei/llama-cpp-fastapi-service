import json
from fastapi import FastAPI
from llama_model import LlamaModel

# Initialize the LlamaModel instance
llama_model_inference = LlamaModel()

# Load the LlamaModel with pre-trained weights or configurations
llama_model_inference.load()

# Quick prediction test to verify if the model has loaded correctly.
# This is useful to check immediately after starting the server.
llama_model_inference.predict(json.dumps({"prompt": "test", "max_tokens": 2}))

# Create an instance of the FastAPI application
app = FastAPI()

@app.post("/predict")
async def predict_text(json_input: dict):
    """
    Endpoint to predict text based on the given input.

    Args:
    - json_input (dict): A dictionary containing input data for the LlamaModel.

    Returns:
    - dict: The model's prediction results.
    """
    result = llama_model_inference.predict(json.dumps(json_input))
    return result

@app.get("/health_check")
async def health_check():
    """
    Health check endpoint to monitor the status of the service.

    Returns:
    - dict: Status and a message indicating if the service is operational.
    """
    return {"status": "ok", "message": "Service is operational"}
