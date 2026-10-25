import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	# Your code here

	r = int((input_height - kernel_height + 2 * padding) / stride) + 1

	result = np.zeros([r,r])

	intp = np.pad(input_matrix, padding)

	for i in range(result.shape[0]):
		for j in range(result.shape[0]):

			region = intp[i * stride : (i * stride) + kernel.shape[0], j * stride : (j * stride) + kernel.shape[0]]
			new = (region * kernel).sum()
			result[i,j] = new



    
	return result
