import numpy as np
import sys
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import warnings
from src.exception import customException
from src.logger import logging
import os
from dataclasses import dataclass

from src.utils import save_obj,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts',"model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_train_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting and test input data")
            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1],

            )
            models = {
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Linear Regression":LinearRegression(),
                "K Nearest Neighbors":KNeighborsRegressor(),
                "Gradient Boosting Regressor":GradientBoostingRegressor(),
                "XGBRegressor":XGBRegressor(),
                "CatBoostRegressor":CatBoostRegressor(verbose=False),
                "AdaBoostRegressor":AdaBoostRegressor(),

            }

            model_report:dict = evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
            
            ##To get Best Model 
            best_model_score = max(sorted(model_report.values()))

            ##To get Best Model Name
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_models = models[best_model_name]

            if best_model_score<0.6:
                raise customException("Model Score is less than 0.6")
            logging.info(f"Best Model Found On Training and Testing Test")

            save_obj(
                file_path=self.model_train_config.trained_model_file_path,
                obj = best_models
            )

            predicted = best_models.predict(x_test)

            r2_score_1 = r2_score(y_test,predicted)

            return r2_score_1


        except  Exception as e:
            raise customException(e,sys)


