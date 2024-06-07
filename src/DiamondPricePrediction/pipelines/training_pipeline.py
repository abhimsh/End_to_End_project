from src.DiamondPricePrediction.components.data_ingestion import DataIngestion
from src.DiamondPricePrediction.components.data_transformation import DataTransformation
from src.DiamondPricePrediction.components.model_trainer import ModelTrainer
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.logger import logging


if __name__ == "__main__":
    try:
        data_ingestion_obj = DataIngestion()
        data_transformation_obj = DataTransformation()
        model_tariner_obj = ModelTrainer()

        train_data_path, test_dat_path =  data_ingestion_obj.initiate_data_ingestion()
        train_arr, test_arr = data_transformation_obj.initialize_data_transformation(train_data_path, test_dat_path)
        model_tariner_obj.initiate_model_training(train_arr, test_arr)
    except Exception as error:
            logging.exception(f"Error encountered in Training pipeline, Error: {error}")
            raise CustomException(f"Error in Training pipeline, Error: {error}")
        
