import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import numpy as np
# Problem 13: Concurrent Matrix Multiplication
#
problem = "Description: Create a program that performs matrix multiplication concurrently.\
\
Requirements:\
\
Implement a matrix multiplication system that allows multiple matrix multiplications to be performed concurrently.\
Ensure that matrix multiplications are done correctly and concurrently.\
Test Set:\
\
Provide a set of matrices for multiplication.\
Execute matrix multiplication functions concurrently.\
Verify that matrix multiplications are done correctly."
class MatrixMultiplier:
    def __init__(self):
        self.result_matrices = []
        self.lock = threading.Lock()

    def multiply_matrices(self, matrix1, matrix2):
        with self.lock:
            result_matrix = np.dot(matrix1, matrix2)
            self.result_matrices.append(result_matrix)

def test_concurrent_matrix_multiplication(solution_code):
    matrices = [
        np.array([[1, 2], [3, 4]]),
        np.array([[5, 6], [7, 8]]),
        np.array([[9, 10], [11, 12]]),
    ]
    matrix_multiplier = MatrixMultiplier()

    # Execute the provided solution_code in separate threads
    def execute_solution(matrix1, matrix2):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for matrix1 in matrices:
            for matrix2 in matrices:
                executor.submit(execute_solution, matrix1, matrix2)

    # Verify the correctness of matrix multiplications
    expected_result = np.dot(matrices[0], matrices[0])  # Example: Multiplying the first matrix with itself
    assert np.array_equal(matrix_multiplier.result_matrices[0], expected_result), "Incorrect matrix multiplication"

    # Run Pylint and ThreadSanitizer
    pylint_output = subprocess.getoutput(f"pylint {solution_code}")
    threadsanitizer_output = subprocess.getoutput(f"ThreadSanitizer {solution_code}")

    # Calculate a score based on pylint and threadsanitizer results
    pylint_score = extract_pylint_score(pylint_output) * 10.0  # Implement your scoring logic
    threadsanitizer_score = score_python_code(threadsanitizer_output)  # Implement your scoring logic

    # Calculate the final score
    final_score = (pylint_score + threadsanitizer_score*9) / 20

    # Output the final score
    print(f"Final Score: {final_score}")

# Example solution code
solution_code = pythonCodeGenerator(problem); """
result = np.dot(matrix1, matrix2)
matrix_multiplier.result_matrices.append(result)
"""

test_concurrent_matrix_multiplication(solution_code)
