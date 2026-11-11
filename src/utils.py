import os
import sys
from src.exeption import CustomException
import dill
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models, parms):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = list(parms.values())[i]
            gs = GridSearchCV(model, param, cv=3, n_jobs=-1, verbose=1, scoring='r2', refit=True)
            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
           
            # model = gs.best_estimator_

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)        