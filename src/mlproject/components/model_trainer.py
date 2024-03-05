
import pandas as pd
import os
from mlproject import logger
from sklearn.ensemble import ExtraTreesClassifier
import joblib
import warnings
warnings.filterwarnings("ignore")
from mlproject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        etmodel = ExtraTreesClassifier(n_estimators=self.config.n_estimators, max_depth=self.config.max_depth, max_leaf_nodes=self.config.max_leaf_nodes, criterion=self.config.criterion, random_state=42)
        etmodel.fit(train_x, train_y)

        joblib.dump(etmodel, os.path.join(self.config.root_dir, self.config.model_name))