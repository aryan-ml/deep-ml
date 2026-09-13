import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	
	c_in = np.linalg.inv(C)
	
	p = np.matmul(c_in, B)
	
	return p

