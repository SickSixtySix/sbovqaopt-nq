'''
Defines the OptimizerResult class.
'''


class OptimizerResult():
    '''
    Implements an optimization result data structure.
    '''
    def __init__(self) -> None:
        # define the number of function evaluations
        self.nfev = None
        
        # define the number of iterations
        self.nit = None
        
        # define the optimal x
        self.x = None
        
        # define the final function value
        self.fun = None
        
        # define the optimizer message
        self.message = None
        
        # define patch centers coordinates
        self.patch_centers_x = []
