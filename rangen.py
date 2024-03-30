import numpy as np
from pathlib import Path

'''
Generates random input.txt file as input for task1.py
'''

def generateSLETXT():
    # Define the size of the system
    rows = 4
    cols = 4
    vars = ['x', 'y', 'z', 'w']

    # Get filepath in case code not run from immediate directory
    outputFilename = "input.txt"
    scriptDirectory = Path(__file__).resolve().parent
    outputFilePath = scriptDirectory / outputFilename

    # Generate random, solvable coefficients and constants
    A = np.random.randint(-10, 10, size=(rows, cols))
    while np.linalg.matrix_rank(A) < rows:
        A = np.random.randint(-10, 10, size=(rows, cols))
    x = np.random.randint(-10, 10, size=cols)
    b = np.dot(A, x)

    # Generate input.txt file
    with open(outputFilePath, 'w') as outfile:
        for i in range(rows):
            equation = " + ".join([f"{A[i][j]}{vars[j]}" for j in range(cols)])
            outfile.write(f"{equation} = {b[i]}\n")

    outfile.close()
    return outputFilePath

if __name__ == "__main__":
    generateSLETXT()