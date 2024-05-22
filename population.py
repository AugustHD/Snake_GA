population_size = 10  # Number of individuals in the population
gene_length = 1       # Length of each chromosome
gene_min = 0          # Minimum gene value
gene_max = 10         # Maximum gene value

# Initialize a population
def initialize_population(pop_size, gene_length, gene_min, gene_max):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(gene_min, gene_max) for _ in range(gene_length)] # Randomly generate snake's chromosomes (Neural Network weights)
        population.append(chromosome) # Append the chromosome to the population
    return population