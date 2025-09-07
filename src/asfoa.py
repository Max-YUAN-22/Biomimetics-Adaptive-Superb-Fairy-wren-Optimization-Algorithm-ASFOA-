import numpy as np

# Function to initialize population
def initialize_population(N, D, lb, ub):
    return lb + np.random.rand(N, D) * (ub - lb)

# Define the ASFOA algorithm here based on the descriptions in the paper
def asfoa(N, D, lb, ub, max_FEs):
    population = initialize_population(N, D, lb, ub)
    best_solution = None
    best_fitness = np.inf

    FEs = 0
    while FEs < max_FEs:
        # Implement the three strategies: ASF, TSG, ADS
        pass  # Placeholder for the ASFOA algorithm steps

    return best_solution, best_fitness
