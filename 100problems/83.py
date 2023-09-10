import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
from cryptography.fernet import Fernet
# Problem 78: Concurrent Data Encryption
#
problem = "Description: Build a program to concurrently encrypt sensitive data using multiple encryption algorithms.\
\
Requirements:\
\
Implement a data encryption system that allows multiple pieces of data to be encrypted concurrently using different encryption algorithms.\
Ensure that data encryption is performed correctly and concurrently.\
Test Set:\
\
Provide a list of data pieces and encryption algorithms.\
Execute encryption functions concurrently.\
Verify that data is encrypted correctly."
class DataEncryptor:
    def __init__(self):
        self.encrypted_data = []
        self.lock = threading.Lock()

    def encrypt_data(self, data, encryption_algorithm):
        with self.lock:
            # Simulate data encryption using different algorithms
            if encryption_algorithm == "AES":
                key = Fernet.generate_key()
                fernet = Fernet(key)
                encrypted_data = fernet.encrypt(data.encode())
                self.encrypted_data.append((data, encryption_algorithm, encrypted_data))

def test_concurrent_data_encryption(solution_code):
    data_and_algorithms = [
        ("SensitiveInfo1", "AES"),
        ("SensitiveInfo2", "RSA"),
        ("SensitiveInfo3", "AES"),
    ]
    data_encryptor = DataEncryptor()

    # Execute the provided solution_code in separate threads
    def execute_solution(data, encryption_algorithm):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for data, encryption_algorithm in data_and_algorithms:
            executor.submit(execute_solution, data, encryption_algorithm)

    # Verify the correctness of data encryption
    for data, algorithm, encrypted_data in data_and_algorithms:
        # assert (data, algorithm, encrypted_data) in data_encryptor.encrypted_data, f"Incorrect data encryption: {data}, {algorithm}"

    # Run Pylint and ThreadSanitizer
    pylint_output = subprocess.getoutput(f"pylint {solution_code}")
    threadsanitizer_output = subprocess.getoutput(f"ThreadSanitizer {solution_code}")

    # Calculate a score based on pylint and threadsanitizer results
    pylint_score = extract_pylint_score(pylint_output)  # Implement your scoring logic
    threadsanitizer_score = score_python_code(threadsanitizer_output)  # Implement your scoring logic

    # Calculate the final score
    final_score = (pylint_score*3 + float(threadsanitizer_score)*7) / 10

    # Output the final score
    print(f"Final Score: {final_score}")

# Example solution code
solution_code = pythonCodeGenerator(problem); """
data_encryptor.encrypt_data(data, encryption_algorithm)
"""

test_concurrent_data_encryption(solution_code)
