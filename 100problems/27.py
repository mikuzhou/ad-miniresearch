import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 25: Concurrent Sensor Readings
#
problem = "Description: Design a program for reading sensor data concurrently.\
\
Requirements:\
\
Implement a sensor reading system that allows multiple sensors to read data concurrently.\
Ensure that sensor data is read correctly and concurrently.\
Test Set:\
\
Simulate multiple sensors reading data concurrently.\
Verify that the sensor data is read correctly."
class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.data = 0
        self.lock = threading.Lock()

    def read_data(self):
        with self.lock:
            # Simulate sensor data reading
            self.data += 1
            return self.data

def test_concurrent_sensor_readings(solution_code):
    sensors = [Sensor(1), Sensor(2), Sensor(3)]

    # Execute the provided solution_code in separate threads to read sensor data
    def read_sensor_data(sensor):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for sensor in sensors:
            executor.submit(read_sensor_data, sensor)

    # Verify the correctness of sensor data reading
    time.sleep(1)  # Give threads some time to read data
    sensor_data = [sensor.read_data() for sensor in sensors]
    expected_data = [1, 2, 3]  # Expected sensor data after reading
    assert sensor_data == expected_data, "Incorrect sensor data reading"

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
sensor_data.append(sensor.read_data())
"""

test_concurrent_sensor_readings(solution_code)
