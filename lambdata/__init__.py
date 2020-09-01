"""lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

TEST = pd.DataFrame(np.ones(10))

def df_cleaner(df):
    """Clean a dataframe!"""
    pass # TODO -implement

def check_nulls(df):
    na_counts = df.isnull().sum()
    pass na_counts

def train_val_split(X, y, test_size, random_state):
    X_train, X_val, y_train, y_val = train_test_split(X, y test_size=test_size, random_state=random_state) 
    pass X_train, X_val, y_train, y_val

