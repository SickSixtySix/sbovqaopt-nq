'''
Tests for sbovqaopt.optimizer module.
'''
from sbovqaopt_nq.optimizer import Optimizer

import numpy as np
import matplotlib.pyplot as plt


def main():
    def objective(x: np.ndarray) -> float:
        return np.linalg.norm(x)
    x0 = np.array([0.05, 0.04, 0.03, 0.02])

    # test with nfev_final_avg=20, verify res.x and res.fun
    #optimizer = Optimizer(patch_size=0.01, nfev_final_avg=20)
    #res = optimizer.minimize(objective, x0)
    #assert np.all(np.isclose(res.x, np.zeros_like(x0), atol=0.01))
    #assert np.isclose(res.fun, 0, atol=0.01)

    #optimizer = Optimizer(patch_size=0.01, nfev_final_avg=20)
    #res = optimizer.minimize(objective, x0)
    #print(vars(res))
    
    #optimizer = Optimizer(patch_size=0.01, nfev_final_avg=20)
    #res = optimizer.minimize(objective, x0, options={'gtol': 1e-5})
    #print(vars(res))
    
    optimizer = Optimizer(patch_size=0.1, npoints_per_patch=100, nfev_final_avg=0)
    res = optimizer.minimize(objective, x0)
    print(res.message)
    print(res.x)
    print(res.nit)
    norm_x = []
    for j in range(1, len(res.patch_centers_x)):
        norm_x = norm_x + [np.linalg.norm(res.patch_centers_x[j] - res.patch_centers_x[j - 1])]
    plt.plot(norm_x)

    # test with nfev_final_avg=0, verify that no res.fun is returned
    #optimizer = Optimizer(patch_size=0.01, nfev_final_avg=0)
    #res = optimizer.minimize(objective, x0)
    #assert isinstance(res.fun, str)

if __name__ == "__main__":
    main()