'''2. Convert the below list into a numpy array then display the array then
display the first and last index and then multiply each element by 2 and
display the result.

Input: my_list = [1, 2, 3, 4, 5]'''
import numpy as np

# Convert the list to a NumPy array
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

# Display the array
print("NumPy Array:", my_array)

# Display the first and last index elements
print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2
result_array = my_array * 2
print("Array after multiplying each element by 2:", result_array)
