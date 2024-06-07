from dataclasses import dataclass
import os
from collections import OrderedDict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.utils.utils import save_object
from src.DiamondPricePrediction.utils.utils import evaluate_all_models

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("Initiate model training")
            X_train, X_test, y_train, y_test = (
                train_arr[:, :-1],
                test_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, -1]
            )
            # List of all models to train and check
            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet()
                }
            
            all_model_report = evaluate_all_models(X_train, X_test, y_train, y_test, models)
            logging.info("All model training completed")

            logging.info("="*50)
            logging.info("Model report")
            logging.info("="*50)

            for model_name, r2_score in all_model_report.items():
                 logging.info(f"{model_name} - {r2_score}")
            
            logging.info("="*50)

            # Find the best model via r2_Score
            best_model_name = None
            best_r2_score = 0
            for model_name, r2_score in all_model_report.items():
                 if r2_score > best_r2_score:
                      best_r2_score = r2_score
                      best_model_name = model_name

            logging.info("=="*50)
            logging.info(f"Best Model : {best_model_name}")
            logging.info(f"Best R2 Score : {best_r2_score}")
            logging.info("=="*50)

            save_object(
                 file_path=self.model_trainer_config.trained_model_path,
                 obj=models[best_model_name]
                 )
            logging.info("best mode obj pickled successfully")

            logging.info("Model training Step completed successfully")
        except Exception as error:
                logging.exception(f"Error encountered while performing Model training, Error: {error}")
                raise CustomException(f"Error in Model training, Error: {error}")
        