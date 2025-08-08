'''
Tests for sbovqaopt.optimizer module.
'''
from sbovqaopt.optimizer import Optimizer

import numpy as np


def main():
    optimizer = Optimizer()

    def objective(x: np.ndarray) -> float:
        return np.linalg.norm(x)
    x0 = np.array([0.05, 0.04, 0.03, 0.02])

    # Print message
    print(f'x0 = {x0}')

    # test with nfev_final_avg=20, verify res.x and res.fun
    optimizer = Optimizer(patch_size=0.01, nfev_final_avg=20)
    res = optimizer.minimize(objective, x0)
    assert np.all(np.isclose(res.x, np.zeros_like(x0), atol=0.01))
    assert np.isclose(res.fun, 0, atol=0.01)
    
    # Print message
    print(vars(res))

    # test with nfev_final_avg=0, verify that no res.fun is returned
    optimizer = Optimizer(patch_size=0.01, nfev_final_avg=0)
    res = optimizer.minimize(objective, x0)
    assert isinstance(res.fun, str)
    
    # Print message
    print(vars(res))

if __name__ == "__main__":
    main()