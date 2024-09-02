""" This module contains a class for activation functions """
import numpy as np


class ActivationFunction:
    def __init__(self, x):
        self.x = x

    def sigmoid(self):
        return np.exp(self.x)
