"""Abstract base class for various models"""

from abc import ABCMeta, abstractmethod
from typing import Dict
from sklearn.datasets import make_regression
import numpy as np
import matplotlib.pyplot as plt

class LinearBase(metaclass=ABCMeta):
    """Abstract Base class representing the Linear Model"""
    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

    def make_regression_example(self, n_samples: int=10000, n_features: int=5) -> Dict:
        features, output, coef = make_regression(
            n_samples=n_samples,
            n_features=n_features,
            n_informative=n_features, n_targets=1,
            noise = 5, coef=True)
        return dict(zip(['X','y','coef'], [features, output, coef]))
    
    def make_constant(self, X: np.ndarray) -> np.ndarray: 
        if self.fit_intercept: 
            ones = np.ones(shape=(X.shape[0], 1))
            return np.concatenate((ones, X), axis=1)
        return X

    def reg_plot(self,x,y):
        plt.scatter(x, y, c='steelblue', edgecolor='white', s=70)
        plt.plot(x, self.predictions, color='yellow', lw=2)