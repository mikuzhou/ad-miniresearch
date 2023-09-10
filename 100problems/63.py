import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
from PIL import Image
# Problem 58: Concurrent Image Compression
#
problem = "Description: Build a program to concurrently compress a batch of images.\
\
Requirements:\
\
Implement an image compression system that allows multiple images to be compressed concurrently.\
Ensure that image compression is performed correctly and concurrently.\
Test Set:\
\
Provide a list of images to compress.\
Execute compression functions concurrently.\
Verify that all images are compressed correctly."
class ImageCompressor:
    def __init__(self):
        self.compressed_images = []
        self.lock = threading.Lock()

    def compress_image(self, image_path, output_path):
        with self.lock:
            # Implement image compression logic here
            img = Image.open(image_path)
            img.save(output_path, "JPEG", quality=50)
            self.compressed_images.append(output_path)

def test_concurrent_image_compression(solution_code):
    images_to_compress = [
        ("image1.jpg", "compressed1.jpg"),
        ("image2.jpg", "compressed2.jpg"),
        ("image3.jpg", "compressed3.jpg"),
    ]
    image_compressor = ImageCompressor()

    # Execute the provided solution_code in separate threads
    def execute_solution(image_path, output_path):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for image_path, output_path in images_to_compress:
            executor.submit(execute_solution, image_path, output_path)

    # Verify the correctness of image compression
    for _, compressed_image_path in images_to_compress:
        # assert compressed_image_path in image_compressor.compressed_images, f"Incorrect image compression: {compressed_image_path}"

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
image_compressor.compress_image(image_path, output_path)
"""

test_concurrent_image_compression(solution_code)
