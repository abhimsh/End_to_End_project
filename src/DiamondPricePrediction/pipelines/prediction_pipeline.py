import os
import pandas as pd
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.utils.utils import load_object
from src.DiamondPricePrediction.components.data_transformation import DataTransformerConfig
from src.DiamondPricePrediction.components.model_trainer import ModelTrainerConfig

class PredictPipeline:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()
        self.data_transformation_config = DataTransformerConfig()

    def predict(self, all_features):
        try:
            # Load the preprocessor and model objects from the pickle files
            preprocessor_obj = load_object(self.data_transformation_config.preprocessor_obj_file_path)
            model_obj = load_object(self.model_trainer_config.trained_model_path)
            logging.info("Loaded the preprocessor obj and model obj from pickle files")

            # Perform preprocessing of the data
            processed_data = preprocessor_obj(all_features)
            logging.debug("Processed data : {}".format(processed_data))

            # Perform Prediction on the received data
            predicted_value = model_obj.predict(processed_data)
            logging.debug("Prediction : {}".format(predicted_value))

            return predicted_value
        
        except Exception as error:
            logging.exception(f"Error encountered while Prediction, Error: {error}")
            raise CustomException(f"Error in Prediction, Error: {error}")
        

class CustomData:
    def __init__(
            self,
            carat: float,
            depth: float,
            table: float,
            x: float,
            y: float,
            z: float,
            cut: str,
            color: str,
            clarity: str
            ) -> None:
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity
    
    def get_data_as_dataframe(self):
        try:
            data_dictionary = {
                "carat": [self.carat],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y": [self.y],
                "z": [self.z],
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity]
            }

            data = pd.DataFrame(data_dictionary)
            logging.info(f"Data Frame create successfully \n {data.to_string()}")
            return data
        except Exception as error:
            logging.exception(f"Error encountered while converting data to dataframe, Error: {error}")
            raise CustomException(f"Error in Conversion to DataFrame, Error: {error}")
        