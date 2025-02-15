
## filter matrix 

import numpy as np 

# np.random.seed(42)

def filterMatrix(matrix):
    # Replace elements greater than 25 with 0
    matrix[matrix > 25] = 0
    print("Filtered Matrix:\n", matrix)
    print("Sum:\n", np.sum(matrix))
    print("mean: \n", np.mean(matrix))
    print("devition: \n", np.std(matrix))
    
    
matrix = np.random.randint(1,50, size=(5,5))
filterMatrix(matrix)
print(matrix)

