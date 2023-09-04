import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
# Problem 7: Concurrent Task Execution
#
# Description: Create a program that performs multiple tasks concurrently and tracks their completion.
#
# Requirements:
#
# Implement a task execution system that allows multiple tasks to run concurrently.
# Track the completion status of each task.
# Ensure that tasks are executed correctly and concurrently.
# Test Set:
#
# Define a set of tasks (e.g., functions to calculate factorial or sum numbers).
# Execute these tasks concurrently and track their completion.
# Verify that all tasks complete successfully.
class TaskExecutor:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()

    def add_task(self, task_function, *args, **kwargs):
        with self.lock:
            self.tasks.append((task_function, args, kwargs))

    def execute_tasks(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(task_function, *args, **kwargs) for task_function, args, kwargs in self.tasks]
        return [future.result() for future in futures]

def test_concurrent_task_execution(solution_code):
    task_executor = TaskExecutor()

    # Execute the provided solution_code to add tasks
    def add_tasks():
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(10):
            executor.submit(add_tasks)

    # Execute the tasks concurrently
    results = task_executor.execute_tasks()

    # Check correctness
    assert all(result is not None for result in results), "Some tasks failed"

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
solution_code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

task_executor.add_task(factorial, 5)
"""

test_concurrent_task_execution(solution_code)
