import pickle
import os
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.logger import logging


def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as error:
        logging.exception(f"Error encountered while writting the obj from pickled file, Error: {error}")
        raise CustomException(f"Error in Data Write to pickle file, Error: {error}")
        

def load_object(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} Not Found!!")
        
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as error:
        logging.exception(f"Error encountered while reading the obj from pickled file, Error: {error}")
        raise CustomException(f"Error inData Read from pickle file, Error: {error}")
        

def evaluate_all_models(X_train, X_test, y_train, y_test, models_dict):
    try:
        reports = {}
        for model, model_obj in models_dict.items():
            model_obj.fit(X_train, y_train)
            test_r2_score = model_obj.score(X_test, y_test)
            reports[model] = test_r2_score
        
        return reports
    except Exception as error:
        logging.exception(f"Error encountered while Evaluating Models using r2_score, Error: {error}")
        raise CustomException(f"Error in Model Evaluation, Error: {error}")
