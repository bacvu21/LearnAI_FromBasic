## modify and print even number or modified value in array 
import numpy as np 
# arr = np.array([1,5,4,2,6,9])

# eventArr = arr[arr % 2 ==0]
# print("eventArr: ", eventArr)

# modified = arr[arr > 3]
# print("modified Array: ", modified)

#### random arr
### settings seed by fixing number of sequence fixed 

np.random.seed(2)

randArr = np.random.rand(3,3)

inteArr = np.random.randint(0,10, size=(2,3))

print("random array: \n",randArr )
print("random but Integer Value: \n", inteArr)