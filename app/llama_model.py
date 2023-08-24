import json
from llama_cpp import Llama
from huggingface_hub import hf_hub_download
from config import logger


class LlamaModel:
    """
    A class to represent the Llama Model for inference.

    Attributes:
    - loaded (bool): If the model has been loaded or not.
    - lcpp_llm (object): Instance of the Llama C++ model.
    - model_path (str): Path to the model's location.
    """

    def __init__(self):
        """Initialize a new instance of the LlamaModel class."""
        self.loaded = False
        self.lcpp_llm = None
        self.model_path = ""

    def load(self, model_name_or_path="TheBloke/Llama-2-13B-chat-GGML",
             model_basename="llama-2-13b-chat.ggmlv3.q5_1.bin"):
        """
        Load the Llama model from the given path or name.

        Args:
        - model_name_or_path (str): Identifier for the model on HuggingFace Hub.
        - model_basename (str): Base name for the model file.
        """
        logger.info("===== [ Start  ] Load Llama 2 model. =====")
        self.model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)
        logger.info("===== [ Finish ] Load Llama 2 model. =====")

    def predict(self, data):
        """
        Predict the output for the given data using the Llama model.

        Args:
        - data (str): JSON formatted string containing input data.

        Returns:
        - dict: Predicted answer.
        """
        # Check if the model is already loaded.
        if not self.loaded:
            self.loaded = True
            self.lcpp_llm = Llama(
                model_path=self.model_path,
                n_threads=2,
                n_batch=512,
                n_gpu_layers=32,
                verbose=False
            )

        logger.info("===== [ Start  ] Prediction. =====")
        
        # Deserialize the JSON string into a dictionary
        data_dict = json.loads(data)
        logger.info("[ Prompt ] {}.".format(data_dict))
        
        # Invoke the model for prediction
        response = self.lcpp_llm(
            prompt=data_dict['prompt'],
            max_tokens=data_dict['max_tokens'],
            temperature=0.5,
            top_p=0.95,
            repeat_penalty=1.2,
            top_k=150,
            echo=True
        )
        
        logger.info("[ Result ] {}.".format(response))
        logger.info("===== [ Finish ] Prediction. =====")

        return {"answer": response["choices"][0]["text"]}
