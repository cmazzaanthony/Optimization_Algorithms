import unittest

import numpy as np

from coptim.functions.mse import MSE
from coptim.functions.l1 import L1
from coptim.optimizers.proximal_gradient_method import ProximalGradientMethod


class TestProximalGradientMethod(unittest.TestCase):

    def test_lasso(self):
        np.random.seed(42)

        n_samples, n_features = 50, 100
        X = np.random.randn(n_samples, n_features)

        idx = np.arange(n_features)
        coef = (-1) ** idx * np.exp(-idx / 10)
        coef[10:] = 0
        y = np.dot(X, coef)

        optimizer = ProximalGradientMethod()
        sfunc = MSE(X, y)
        nsfunc = L1(0.05)

        starting_point = np.zeros(n_features)
        step_size = 0.1
        epsilon = 1e-2

        x = optimizer.optimize(starting_point,
                               sfunc,
                               nsfunc,
                               step_size,
                               epsilon)

        self.assertEqual(np.count_nonzero(x), 9)
        self.assertEqual(optimizer.iterations, 21)
