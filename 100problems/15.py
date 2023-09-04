import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 15: Concurrent Task Scheduler
#
# Description: Design a task scheduler that allows multiple tasks to be scheduled and executed concurrently.
#
# Requirements:
#
# Implement a task scheduling system that allows multiple tasks to be scheduled and executed concurrently.
# Ensure that tasks are executed correctly and concurrently.
# Test Set:
#
# Define a set of tasks with different execution times.
# Schedule these tasks to run concurrently using the task scheduler.
# Verify that tasks are executed correctly within their specified times.
class TaskScheduler:
    def __init__(self):
        self.completed_tasks = []
        self.lock = threading.Lock()

    def schedule_task(self, task_name, execution_time):
        time.sleep(execution_time)
        with self.lock:
            self.completed_tasks.append(task_name)

def test_concurrent_task_scheduler(solution_code):
    task_scheduler = TaskScheduler()

    # Execute the provided solution_code in separate threads to schedule tasks
    def schedule_tasks():
        exec(solution_code)

    tasks = [("Task1", 2), ("Task2", 1), ("Task3", 3)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(3):
            executor.submit(schedule_tasks)

    # Verify the correctness of task execution
    time.sleep(5)  # Give threads some time to complete tasks
    completed_tasks = task_scheduler.completed_tasks
    expected_tasks = ["Task2", "Task1", "Task3"]  # Expected order of completed tasks
    assert completed_tasks == expected_tasks, "Incorrect task execution order"

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
task_scheduler.schedule_task(task_name, execution_time)
"""

test_concurrent_task_scheduler(solution_code)
