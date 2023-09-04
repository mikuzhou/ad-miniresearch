import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 41: Concurrent Task Scheduler
#
# Description: Design a program to concurrently schedule and execute tasks.
#
# Requirements:
#
# Implement a task scheduling system that allows multiple tasks to be scheduled and executed concurrently.
# Ensure that tasks are executed correctly and concurrently.
# Test Set:
#
# Provide a list of tasks with their execution times.
# Execute tasks concurrently.
# Verify that all tasks are executed correctly.
class TaskScheduler:
    def __init__(self):
        self.completed_tasks = []
        self.lock = threading.Lock()

    def execute_task(self, task_name, execution_time):
        with self.lock:
            # Implement task execution logic here
            time.sleep(execution_time)  # Simulate task execution
            self.completed_tasks.append(task_name)

def test_concurrent_task_scheduler(solution_code):
    tasks = [("Task1", 2), ("Task2", 3), ("Task3", 1)]
    task_scheduler = TaskScheduler()

    # Execute the provided solution_code in separate threads
    def execute_solution(task_name, execution_time):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for task_name, execution_time in tasks:
            executor.submit(execute_solution, task_name, execution_time)

    # Verify the correctness of task execution
    assert all(task_name in task_scheduler.completed_tasks for task_name, _ in tasks), "Incorrect task execution"

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
task_scheduler.execute_task(task_name, execution_time)
"""

test_concurrent_task_scheduler(solution_code)
