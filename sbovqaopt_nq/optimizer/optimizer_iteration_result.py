'''
Defines the OptimizerIterationResult class.
'''


class OptimizerIterationResult():
    '''
    Implements an optimization iteration result data structure.
    '''
    def __init__(self) -> None:
        # the expectation gradients at the patch center
        self.grad_exp_z = None
        
        # the underlying optimization result
        self.kde_opt_res = None
