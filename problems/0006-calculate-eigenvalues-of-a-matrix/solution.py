import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	A = np.array(matrix)
	eigenvalues = np.linalg.eigvals(A)

	
	
	return eigenvalues