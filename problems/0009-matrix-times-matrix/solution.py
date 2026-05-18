import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    p = np.shape(a)[1]
    q = np.shape(b)[0]

    if p == q:
        return np.dot(a,b)
    else:
        return -1
