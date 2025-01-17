import numpy as np

array = np.array([1, 2, 3, 4, 5])

#compute the sum of all elements:
array_sum = np.sum(array)

#finding the mean and standard deviation
array_mean = np.mean(array)
array_std = np.std(array)

#Multiply each element by 2
array_multiplied = array * 2

# Print the results
print(f"Original Array: {array}")
print(f"Sum of elements: {array_sum}")
print(f"Mean of elements: {array_mean}")
print(f"Standard Deviation: {array_std}")
print(f"Array after multiplication by 2: {array_multiplied}")
