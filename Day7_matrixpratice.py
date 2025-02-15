import numpy as np



def normalize_matrix(matrix): 
    
    
    minValue = np.min(matrix)
    maxValue = np.max(matrix)
    x_ = (matrix - minValue) / (maxValue - minValue)
    return x_



#normalize matrix ? => convert into 


defaulMatrix = np.array([[1,1,3,4], [4,5,3,1], [7,5,4,3], [8,0,1,2]])

mormalMatrix = normalize_matrix(defaulMatrix)

print(mormalMatrix)