def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps):
    
        # forward pass
        fwd = (a * x0**2) + (b * x0) + c 
    
        # backward pass 
        grad = (2 * a * x0) + b 
    
        # update step
        x0 += lr * -grad 
    return x0 