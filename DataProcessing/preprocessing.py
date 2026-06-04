import numpy as np
from sklearn import preprocessing 

input_data = np.array([[2.1, -1.9, 5.5],
 [-1.5, 2.4, 3.5],
 [0.5, -7.9, 5.6],
 [5.9, 2.3, -5.8]])

data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)
print("\n")
print("Mean =", input_data.mean(axis=0))
print("Std deviation = ", input_data.std(axis=0))
print("\n")
