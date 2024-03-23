# Task #1 - System of Linear Equations
import numpy as np
import re
import rangen

# generates a random, solvable system of linear equations as a txt file
# and saves the path to inputPath
inputPath = rangen.generateSLETXT()
matrix = []
ps = []
pattern = r'-?\d+\.?\d*'
print("Task #1 - System of Linear Equations\n")
print(f"Input from {inputPath}\n")
with open(inputPath, 'r', newline='') as file:
    for row in file:
        # gets equation from row (ex. 4x + 1y + -3z + -3w = -55)
        equation = row.strip()
        print(equation)
        # gets list of numbers as strings, convert to list of floats
        nums = re.findall(pattern, equation)
        nums = [float(num) for num in nums]
        # takes the last element and adds it to the P list
        ps.append(nums.pop())
        # adds the list generated from the equation minus the last element to the matrix
        matrix.append(nums)
    file.close()

# solve
A = np.array(matrix)
A_inv = np.linalg.inv(A)
solution = np.dot(A_inv, ps)

# output
print("\nSolution:")
print(f"x = {solution[0]:.2f}")
print(f"y = {solution[1]:.2f}")
print(f"z = {solution[2]:.2f}")
print(f"w = {solution[3]:.2f}")