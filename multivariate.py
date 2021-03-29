import pandas as pd
import numpy as np

# Import datasets
train = pd.read_csv('lebron_train.csv')
test = pd.read_csv('lebron_test.csv')

# Target variable, winning or losing
train_result = train['Result'].tolist()
test_result = test['Result'].tolist()

# Predict which individual variable is the best predictor of Lebron winning
def singleVariable():
    pass

# Predict which two variables combined best predict Lebron winning
def twoVariables():
    pass