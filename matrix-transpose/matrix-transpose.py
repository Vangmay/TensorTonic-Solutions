import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    x, y = np.array(A).shape 
    ans = np.zeros((y, x))

    for i in range(x):
        for j in range(y):
            ans[j][i] = A[i][j] 
    return ans
        
