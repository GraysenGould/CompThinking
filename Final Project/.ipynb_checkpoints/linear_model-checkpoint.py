import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LinearModel():
    def __init__ (self):
        self.model = LinearRegression()
        self.data = None
        self.xvars = None
        self.yvar = None
        
    def load_dataset(self):
        pass
    def append_dataset(self):
        pass
    def split_data (self):
        pass
    def train (self, X,y):
        pass
    def predict (self):
        pass
    def retrain (self, **args);
        print("Retraining model with updated parameters...")
        return train(**args)
    def interface():
        pass 