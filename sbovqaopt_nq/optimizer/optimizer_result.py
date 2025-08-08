'''
Defines the OptimizerResult class.
'''


class OptimizerResult():
    '''
    Implements an optimization result data structure.
    '''
    def __init__(self) -> None:
        # Define the number of function evaluations
        self.nfev = None
        
        # Define the number of iterations
        self.nit = None
        
        # Define the optimal x
        self.x = None
        
        # Define the final function value
        self.fun = None
