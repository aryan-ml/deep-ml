import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""

	if len(v1) != 0 and len(v2) != 0:
		if len(v1) == len(v2):
			num = v1 @ v2
			d = np.linalg.norm(v1) * np.linalg.norm(v2) 
			return (num/d)
			
		else:
			return -1
			
	else:
		return -1




