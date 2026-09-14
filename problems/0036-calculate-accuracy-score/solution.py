import numpy as np

def accuracy_score(y_true, y_pred):


	correct = 0

	for i in range(len(y_true)):
		if y_true[i] == y_pred[i]:
			correct+=1


	avg = correct / len(y_true)

	return avg



