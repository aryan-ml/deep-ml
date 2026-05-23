import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	if (np.linalg.det(T) != 0) and (np.linalg.det(S) != 0):
		inv = np.linalg.inv(T)
		ans = inv @ A @ S 		## Here using @ is same as using np.dot(a, b) 
		return ans 
	else:
		return -1