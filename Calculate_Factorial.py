

def factorial_cal(n): 
    if (n == 0):
        return 1
    return factorial_cal(n-1) * n




test= factorial_cal(3)
print(test)