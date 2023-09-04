import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import random
# Problem 67: Concurrent Sensor Data Processing
#
# Description: Build a program to concurrently process data from multiple sensors.
#
# Requirements:
#
# Implement a sensor data processing system that allows data from multiple sensors to be processed concurrently.
# Ensure that data processing is executed correctly and concurrently.
# Test Set:
#
# Provide a list of sensor data and processing tasks.
# Execute processing functions concurrently.
# Verify that all data is processed correctly.
class SensorDataProcessor:
    def __init__(self):
        self.processed_data = []
        self.lock = threading.Lock()

    def process_data(self, sensor_data, task):
        with self.lock:
            # Simulate data processing with random results
            result = round(random.uniform(0, 100), 2)
            self.processed_data.append((sensor_data, task, result))

def test_concurrent_sensor_data_processing(solution_code):
    sensor_data_and_tasks = [
        (10.5, "Temperature"),
        (25.0, "Pressure"),
        (60.3, "Humidity"),
    ]
    sensor_processor = SensorDataProcessor()

    # Execute the provided solution_code in separate threads
    def execute_solution(sensor_data, task):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for sensor_data, task in sensor_data_and_tasks:
            executor.submit(execute_solution, sensor_data, task)

    # Verify the correctness of data processing
    for sensor_data, task, _ in sensor_data_and_tasks:
        assert (sensor_data, task, _) in sensor_processor.processed_data, f"Incorrect data processing: {sensor_data}, {task}"

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
sensor_processor.process_data(sensor_data, task)
"""

test_concurrent_sensor_data_processing(solution_code)
