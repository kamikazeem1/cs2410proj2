import numpy as np
import time
import os

def generateSLETXT():
    # Define the size of the system
    num_variables = 4  # Number of variables
    num_equations = 4  # Number of equations
    vars = ['x', 'y', 'z', 'w']

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = "input.txt"
    output_file_path = os.path.join(script_dir, output_filename)


    # Generate random coefficients and constants
    A = np.random.randint(-10, 10, size=(num_equations, num_variables))
    while np.linalg.matrix_rank(A) < num_equations:
        A = np.random.randint(-10, 10, size=(num_equations, num_variables))
    x = np.random.randint(-10, 10, size=num_variables)
    b = np.dot(A, x)

    with open(output_file_path, 'w') as outfile:
        for i in range(num_equations):
            equation = " + ".join([f"{A[i][j]}{vars[j]}" for j in range(num_variables)])
            outfile.write(f"{equation} = {b[i]}\n")

        currentTime = time.localtime()
        formattedTime = time.strftime("%m/%d/%Y %H:%M:%S", currentTime)
        # outfile.write(f"\nGenerated on {formattedTime}")

    outfile.close()
    return output_file_path

if __name__ == "__main__":
    generateSLETXT()