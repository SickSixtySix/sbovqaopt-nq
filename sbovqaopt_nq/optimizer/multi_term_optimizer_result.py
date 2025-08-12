'''
Defines the MultiTermOptimizerResult class.
'''
from .optimizer_result import OptimizerResult


class MultiTermOptimizerResult(OptimizerResult):
    '''
    Implements an optimization result data structure.
    '''
    def __init__(self) -> None:
        super().__init__()
        
        # Define the optimal y
        self.y = None
