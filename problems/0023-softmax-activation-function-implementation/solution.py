import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    x = np.array(scores, dtype=np.float32)
    maxx = np.max(x)

    return np.exp(x - maxx) / np.sum(np.exp(x - maxx)).tolist()


    