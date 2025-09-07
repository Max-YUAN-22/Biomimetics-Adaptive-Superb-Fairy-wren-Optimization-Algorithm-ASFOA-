import unittest
from src.asfoa import asfoa

class TestASFOA(unittest.TestCase):
    def test_initialization(self):
        N = 30
        D = 10
        lb = -100
        ub = 100
        population = initialize_population(N, D, lb, ub)
        self.assertEqual(population.shape, (N, D))

    def test_best_solution(self):
        N = 30
        D = 10
        lb = -100
        ub = 100
        max_FEs = 1000 * D
        best_solution, best_fitness = asfoa(N, D, lb, ub, max_FEs)
        self.assertIsNotNone(best_solution)
        self.assertTrue(best_fitness <= 0)

if __name__ == '__main__':
    unittest.main()
