import math
import numpy as np

def sigmoid(z: float) -> float:
	#Your code 


	result = 1/(1+math.exp(-z))

	return result