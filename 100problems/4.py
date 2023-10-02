import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import random
# Problem 4: Parallel Sorting Algorithm
#

# Automated Testing Python Code (Simplified):
problem = "Description: Create a program that sorts a list of numbers concurrently using a parallel sorting algorithm.\
\
Requirements:\
\
Implement a parallel sorting algorithm.\
Ensure that the sorting algorithm is correct and thread-safe.\
Test Set:\
\
Sort a list of random numbers concurrently."
class ParallelSorter:
    def __init__(self):
        self.sorted_numbers = None
        self.lock = threading.Lock()

    def parallel_sort(self, numbers):
        with self.lock:
            self.sorted_numbers = sorted(numbers)

def test_parallel_sorting(solution_code):
    numbers = [random.randint(1, 100) for _ in range(100)]
    parallel_sorter = ParallelSorter()

    # Execute the provided solution_code in a separate thread
    def execute_solution():
        exec(solution_code)

    thread = Thread(target=execute_solution)
    thread.start()
    thread.join()

    # Test correctness
    expected_sorted_numbers = sorted(numbers)
    # assert parallel_sorter.sorted_numbers == expected_sorted_numbers, "Incorrect sorting"

    # Run Pylint and ThreadSanitizer
    pylint_output = subprocess.getoutput(f"pylint {solution_code}")
    threadsanitizer_output = subprocess.getoutput(f"ThreadSanitizer {solution_code}")

    # Calculate a score based on pylint and threadsanitizer results
    pylint_score = extract_pylint_score(pylint_output)  # Implement your scoring logic
    threadsanitizer_score = score_python_code(threadsanitizer_output)  # Implement your scoring logic

    # Calculate the final score
    final_score = (pylint_score*3 + float(threadsanitizer_score)*7)  

    # Output the final score
    print(f"Final Score: {final_score}")

# Example solution code
solution_code = pythonCodeGenerator(problem); """
parallel_sorter = ParallelSorter()
numbers = [random.randint(1, 100) for _ in range(100)]
parallel_sorter.parallel_sort(numbers)
"""
test_parallel_sorting(solution_code)
