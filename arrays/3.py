import numpy as np

#Multiply every element in array with 3

array = [2,5,6,8]

an_array= np.array(array)
multiplied_list= an_array * 3


#Extra practice: Multiplying all array elements using NumPy
print(multiplied_list)

an_array = np.prod(array)

print(an_array)
