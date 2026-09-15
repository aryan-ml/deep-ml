import torch

def grad_wss(w_list, x_list):
    """Build w (requires_grad) and x from lists, compute
    loss = 0.5 * sum((w * x)**2), backward, return w.grad
    as a list of floats rounded to 4 decimals.
    """
    
    x = torch.tensor(x_list)
    w = torch.tensor(w_list, requires_grad = True)

    loss = torch.sum((w * x) ** 2) / 2

    loss.backward()

    return w.grad.round(decimals=4).tolist()  