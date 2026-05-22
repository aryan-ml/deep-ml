import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	if mode == 'column':
		mode = 0
	else:
		mode = 1	
	means = np.mean(matrix, axis=mode)

	
	return means

