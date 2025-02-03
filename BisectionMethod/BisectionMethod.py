import sys
sys.path.insert(0, '../')

import GeneralNumericalMethods as gnm
import sympy as sym

class BisectionMethod(gnm.NumericalFunction):
    def __init__(self, function_expression, cutoff_precision, left, right):
        super().__init__(function_expression, cutoff_precision)
        self.left = left
        self.right = right
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def calculate_numerical_method(self):
        user_function = gnm.create_function_from_string(self.function_expression)
        if user_function(self.left) * user_function(self.right) >= 0:
            print("No root could be detected from the intervall")
            return None

        self.number_iterations = 0
        mid = None
        error = 100
        current_function_value = 0
        previous_function_value = 0
        while error > self.cutoff_precision:
            mid = (self.left + self.right) / 2
            self.number_iterations += 1

            if user_function(self.left) * user_function(mid) < 0:
                self.right = mid
            elif user_function(mid) * user_function(self.right) < 0:
                self.left = mid
            else:
                break

            previous_function_value = current_function_value
            current_function_value = user_function(mid)

            error = abs(previous_function_value - current_function_value)
        
        return mid

def main():
    gnm.hello()
    functionExpression = "x**3 - 1 + tan(x)"
    bisection = BisectionMethod(functionExpression, 0.001, -1, 2)
    foundRoot = bisection.calculate_numerical_method()

    if foundRoot != None:
        print(f"The root of {functionExpression}  is at x = {foundRoot:.5f}. It took {bisection.number_iterations} iterations to find.")

if __name__ == '__main__':
    main()
