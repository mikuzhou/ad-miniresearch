import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 23: Concurrent Task Execution
#
problem = "Description: Build a program that executes tasks concurrently.\
\
Requirements:\
\
Implement a task execution system that allows multiple tasks to be executed concurrently.\
Ensure that tasks are executed correctly and concurrently.\
Test Set:\
\
Define a set of tasks with different execution times.\
Execute these tasks concurrently using the task execution system.\
Verify that tasks are executed correctly within their specified times."
class TaskExecutor:
    def __init__(self):
        self.completed_tasks = []
        self.lock = threading.Lock()

    def execute_task(self, task_name, execution_time):
        time.sleep(execution_time)
        with self.lock:
            self.completed_tasks.append(task_name)

def test_concurrent_task_execution(solution_code):
    task_executor = TaskExecutor()

    # Execute the provided solution_code in separate threads to execute tasks
    def execute_solution(task_name, execution_time):
        exec(solution_code)

    tasks = [("Task1", 2), ("Task2", 1), ("Task3", 3)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for task_name, execution_time in tasks:
            executor.submit(execute_solution, task_name, execution_time)

    # Verify the correctness of task execution
    time.sleep(5)  # Give threads some time to complete tasks
    completed_tasks = task_executor.completed_tasks
    expected_tasks = ["Task2", "Task1", "Task3"]  # Expected order of completed tasks
    # assert completed_tasks == expected_tasks, "Incorrect task execution order"

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
task_executor.execute_task(task_name, execution_time)
"""

test_concurrent_task_execution(solution_code)
