import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 74: Concurrent Task Scheduling
#
problem = "Description: Build a program to concurrently schedule and execute tasks from a task queue.\
\
Requirements:\
\
Implement a task scheduling system that allows multiple tasks to be scheduled and executed concurrently.\
Ensure that tasks are scheduled and executed correctly and concurrently.\
Test Set:\
\
Provide a list of tasks and their execution times.\
Execute tasks concurrently based on their scheduled times.\
Verify that all tasks are executed correctly."
class TaskScheduler:
    def __init__(self):
        self.completed_tasks = []
        self.lock = threading.Lock()

    def schedule_task(self, task_name, execution_time):
        with self.lock:
            # Simulate task execution with sleep
            time.sleep(execution_time)
            self.completed_tasks.append(task_name)

def test_concurrent_task_scheduling(solution_code):
    tasks_and_times = [
        ("Task1", 2),
        ("Task2", 1),
        ("Task3", 3),
    ]
    task_scheduler = TaskScheduler()

    # Execute the provided solution_code in separate threads
    def execute_solution(task_name, execution_time):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for task_name, execution_time in tasks_and_times:
            executor.submit(execute_solution, task_name, execution_time)

    # Verify the correctness of task execution
    for task_name, _ in tasks_and_times:
        # assert task_name in task_scheduler.completed_tasks, f"Task not completed: {task_name}"

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
task_scheduler.schedule_task(task_name, execution_time)
"""

test_concurrent_task_scheduling(solution_code)
