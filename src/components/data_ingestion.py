import os
import sys  # Added missing sys import
import src
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    # Setting a default value makes 'config' optional during initialization
    def __init__(self, config: DataIngestionConfig = DataIngestionConfig()):
        self.ingestion_config = config

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
            # CORRECTED: Added 'r' before the string to fix the invalid escape sequence bug
            df = pd.read_csv(r"C:\WebServer\PythonProject\notebook\data\stud.csv")
            logging.info("Data has been loaded")

            # FIXED: Added exist_ok=True so it doesn't crash if 'artifacts' already exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Train and Test split is initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data has been saved")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            # FIXED: Passed sys so CustomException works correctly
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()