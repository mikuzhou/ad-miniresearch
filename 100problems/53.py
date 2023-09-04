import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import gzip
# Problem 45: Concurrent File Compression
#
# Description: Create a program to concurrently compress a batch of files.
#
# Requirements:
#
# Implement a file compression system that allows multiple files to be compressed concurrently.
# Ensure that file compression is performed correctly and concurrently.
# Test Set:
#
# Provide a list of files to compress.
# Execute file compression functions concurrently.
# Verify that all files are compressed correctly.
class FileCompressor:
    def __init__(self):
        self.compressed_files = []
        self.lock = threading.Lock()

    def compress_file(self, file_name):
        with self.lock:
            # Implement file compression logic here
            with open(file_name, 'rb') as f_in, gzip.open(f_name + '.gz', 'wb') as f_out:
                f_out.writelines(f_in)
            self.compressed_files.append(f_name + '.gz')

def test_concurrent_file_compression(solution_code):
    files_to_compress = ["file1.txt", "file2.txt", "file3.txt"]
    file_compressor = FileCompressor()

    # Execute the provided solution_code in separate threads
    def execute_solution(file_name):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for file_name in files_to_compress:
            executor.submit(execute_solution, file_name)

    # Verify the correctness of file compression
    for file_name in files_to_compress:
        compressed_file = file_name + '.gz'
        assert compressed_file in file_compressor.compressed_files, f"File not compressed: {file_name}"

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
file_compressor.compress_file(file_name)
"""

test_concurrent_file_compression(solution_code)
