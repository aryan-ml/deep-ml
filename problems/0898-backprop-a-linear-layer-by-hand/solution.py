import torch

def linear_backward(grad_output, x, W):
    # TODO: return (grad_input, grad_W, grad_b) for y = x @ W.T + b
    a = grad_output @ W 
    b = grad_output.T @ x
    c = grad_output.sum(dim=0)

    return a, b, c
