import pandas as pd
import numpy as np
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from src.DiamondPricePrediction.exception import CustomException
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.utils.utils import save_object
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from dataclasses import dataclass

@dataclass
class DataTransformerConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self) -> None:
        self.data_transformer_config = DataTransformerConfig()

    def get_transformed_data(self):
        try:
            logging.info("About to start creating pipelinr for Data Transformation process")

            # Names of categorical and Numerical columns in data frame
            numerical_features = ['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_features = ['cut', 'color', 'clarity']

            order_categories = [
                ["Fair", "Good", "Very Good", "Premium" , "Ideal"],
                ["D", "E", "F", "G", "H", "I", "J"], 
                ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
                ]

            
            # Order of direct categorical_columns
            cut_categories = ["Fair", "Good", "Very Good", "Premium" , "Ideal"],
            color_categories = ["D", "E", "F", "G", "H", "I", "J"], 
            clarity_categories = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("standard", StandardScaler())
                ]
            )

            logging.info("Numerical pipeline created successfully")
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("ordinal", OrdinalEncoder(categories=order_categories)),
                    ("standard", StandardScaler())
                ]
            )
            logging.info("Categorical pipeline created successfully")
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", numerical_pipeline, numerical_features),
                    ("cat_pipeline", categorical_pipeline, categorical_features)
                ]
            )
            logging.info("Preprocessor object created successfully")
            return preprocessor

        except Exception as error:
            logging.exception(f"Error encountered while creatinmg pipelin for Data Transformation, Error: {error}")
            raise CustomException(f"Error in Data Transformation, Error: {error}")
        
    def initialize_data_transformation(self, train_data_path, test_data_path):
        try:
            logging.info("About to start the Data Transformation process")
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)
            
            logging.debug("Reading the training and test data")
            logging.debug("\n" + train_data.head().to_string())
            logging.debug("\n" + test_data.head().to_string())

            preprocessor_obj = self.get_transformed_data()
            logging.info("preprocessing obj received successfully")
            
            target_feature = "price"
            features_to_be_dropped = [target_feature, "id"]

            # Drop the target colummn and ID columns as its not required
            train_features_data = train_data.drop(columns=features_to_be_dropped, axis=1)
            test_features_data = test_data.drop(columns=features_to_be_dropped, axis=1)
            
            logging.debug("After removal of ID and PRICE columns the data")
            logging.debug("\n" + train_features_data.head().to_string())
            logging.debug("\n" + test_features_data.head().to_string())
            
            # Get target columns for train and test data
            target_train_feature_data = train_data[target_feature]
            target_test_feature_data = test_data[target_feature]

            # perform feature transformation via pipelines
            logging.info("About to perform preprocessing on training and testing data")
            train_features_processed_data_arr = preprocessor_obj.fit_transform(train_features_data)
            test_features_processed_data_arr = preprocessor_obj.transform(test_features_data)
            logging.info("preprocessing on training and testing data completed successfully")
            
            train_arr = np.c_[train_features_processed_data_arr, np.array(target_train_feature_data)]
            test_arr = np.c_[test_features_processed_data_arr, np.array(target_test_feature_data)]
            
            # save the pipeline obj
            save_object(
                file_path = self.data_transformer_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            ) 
            logging.info("preprocessor obj pickled successfully")
            
            return train_arr, test_arr

        except Exception as error:
            logging.exception(f"Error encountered while performing Data Transformation, Error: {error}")
            raise CustomException(f"Error in Data Transformation, Error: {error}")
        