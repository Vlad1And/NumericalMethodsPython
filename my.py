from datetime import datetime
import numpy as np


name = "Vladyslav"
location = "Canada"


array = np.array([1, 2, 3, 4, 5])


print(f"{name} started programming at {datetime.now()}. {location} is a great place!")
print(f"Here is a simple array created with NumPy: {array}")


array_squared = np.power(array, 2)
print(f"Squares of the array: {array_squared}")


array_sum = np.sum(array)
print(f"The sum of the array elements is: {array_sum}")


print("Hello, World!")
