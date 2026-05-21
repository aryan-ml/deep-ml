import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y =  np.array(y)

	ans = np.linalg.solve(X.T @ X, X.T @ y)
	
	return ans.round(4)


