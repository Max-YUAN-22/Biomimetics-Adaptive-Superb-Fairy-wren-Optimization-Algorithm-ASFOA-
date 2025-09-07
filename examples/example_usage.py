from src.asfoa import asfoa
import numpy as np

# Example usage
N = 30  # Population size
D = 10  # Dimension
lb = -100  # Lower bound of the search space
ub = 100  # Upper bound of the search space
max_FEs = 1000 * D  # Maximum number of function evaluations

best_solution, best_fitness = asfoa(N, D, lb, ub, max_FEs)

print(f"Best solution: {best_solution}")
print(f"Best fitness: {best_fitness}")
