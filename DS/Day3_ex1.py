import numpy as np 

# addtition and broadcast value

defaultMatrix = np.array([[1,2,3], [14,2,45], [4,5,7]])
vector = np.array([1,0,-1])
print("add: \n", defaultMatrix + vector)
print("multiple: \n", (defaultMatrix + vector)*2)