import pandas as pd
import numpy as np
import os
from src.DiamondPricePrediction.logger import logging
from sklearn.model_selection import train_test_split
from src.DiamondPricePrediction.exception import CustomException
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join("artifacts", "raw.csv")
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self) -> None:
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> tuple:
        path_of_data = Path(os.path.join("notebooks/data", "gemstone.csv"))
        logging.info("Data Ingestion in progress")
        try:
            # Create Artificatory Folder
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

            # Read the data from the csv file
            data = pd.read_csv(path_of_data)
            logging.info(f"{path_of_data} was read successfully")
            data.to_csv(self.config.raw_data_path, index=False)
            logging.info(f"{self.config.raw_data_path} Artifacts created successfully")

            # Split the data as train and test
            train_data, test_data = train_test_split(data, test_size=0.3, random_state=22)
            logging.info("Data split into train and test successfully")

            # Create train artificatory
            train_data.to_csv(self.config.train_data_path, index=False)
            logging.info(f"{self.config.train_data_path} Artifacts created successfully")

            # Create test artificatory
            test_data.to_csv(self.config.test_data_path, index=False)
            logging.info(f"{self.config.test_data_path} Artifacts created successfully")

            logging.info("Data Ingestion Step completed successfully")
            
            return self.config.train_data_path, self.config.test_data_path
        
        except Exception as error:
            logging.exception(f"Error Encountered in Data Ingestion step, Error: {error}")
            raise CustomException(f"Error encountered during Data ingestion from {path_of_data}, Error: {error}")