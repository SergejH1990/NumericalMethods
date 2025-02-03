import sys
sys.path.insert(0, '../')

import GeneralNumericalMethods as gnm
import numpy as np

class FixedPointMethod(gnm.NumericalFunction):
    def __init__(self, function_expression, cutoff_precision, initial_value):
        super().__init__(function_expression, cutoff_precision)
        self.initial_value = initial_value
    
    def calculate_numerical_method(self):
        user_function = gnm.create_function_from_string(self.function_expression)

        function_value = self.initial_value
        error = 0
        while error > self.cutoff_precision:
            error = 0

def main():
    gnm.hello()
    functionExpression = "x**3 - 1"
    foundRoot = 5
    fixedPoint = FixedPointMethod(functionExpression, 0.001, 0.5) 

    if foundRoot != None:
        print(f'{"The root of "}{functionExpression}{" is at x = "}{foundRoot:.5f}')

if __name__ == '__main__':
    main()