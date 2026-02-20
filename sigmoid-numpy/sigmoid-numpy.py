import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = -np.array(x)
    x = 1 + np.exp(x)
    x = 1 / x  
    return x