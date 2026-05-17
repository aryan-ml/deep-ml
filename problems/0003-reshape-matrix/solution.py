import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python ;;list after reshaping by using numpy's tolist()

	aka =  np.shape(a)  ## (2,4)
	new_shape		## (4,2)

	if (aka[0] == new_shape[1] and aka[1] == new_shape[0]) or (aka[0] == new_shape[0] and aka[1] == new_shape[1]):
		return np.reshape(a, new_shape)
	else:
		return []
