import numpy as np
from abc import ABC, abstractmethod
from sympy import *

def hello():
    print("first time")

def create_function_from_string(expression):
    def function(x):
        return eval(expression)
    return np.frompyfunc(function, 1, 1)

class NumericalFunction(ABC):
    def __init__(self, function_expression, cutoff_precision):
        self.function_expression = function_expression
        self.cutoff_precision = cutoff_precision
        self.number_iterations = 0

    def set_cutoff(self, cutoff):
        self.cutoff_precision = cutoff

    def set_function_expression(self, function_expression):
        self.function_expression = function_expression
    
    def get_number_iterations(self):
        return self.number_iterations

    @abstractmethod
    def calculate_numerical_method(self):
        pass


