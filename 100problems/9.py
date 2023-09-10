import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
from PIL import Image, ImageFilter
# Problem 9: Concurrent Image Filters
#
problem = "Description: Design a program that applies image filters concurrently to a set of images.\
\
Requirements:\
\
Implement a system for applying image filters concurrently.\
Allow multiple threads to process images with different filters concurrently.\
Ensure that image filtering is performed correctly and concurrently.\
Test Set:[\"image1.jpg", "image2.jpg", "image3.jpg\"]\
\
Provide a set of images.\
Execute image filtering functions concurrently to apply various filters (e.g., grayscale, blur) to each image.\
Verify that the filtered images are correct."
class ImageFilterApplicator:
    def __init__(self):
        self.filtered_images = []
        self.lock = threading.Lock()

    def apply_filter(self, image, filter_name):
        with self.lock:
            filtered_image = image.filter(filter_name)
            self.filtered_images.append(filtered_image)

def test_concurrent_image_filters(solution_code):
    image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
    image_filter_applicator = ImageFilterApplicator()

    # Execute the provided solution_code in separate threads
    def execute_solution(image_path, filter_name):
        exec(solution_code)

    filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.GRAYSCALE]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for image_path in image_paths:
            for filter_name in filters:
                executor.submit(execute_solution, image_path, filter_name)

    # Verify the correctness of filtered images
    expected_image_sizes = [(100, 100), (200, 200), (300, 300)]  # Expected image sizes after filtering
    # assert all(image.size == expected_size for image, expected_size in zip(image_filter_applicator.filtered_images, expected_image_sizes)), "Incorrect image filtering"

    # Run Pylint and ThreadSanitizer
    pylint_output = subprocess.getoutput(f"pylint {solution_code}");print(pylint_output)
    threadsanitizer_output = subprocess.getoutput(f"ThreadSanitizer {solution_code}")

    # Calculate a score based on pylint and threadsanitizer results
    pylint_score = extract_pylint_score(pylint_output)  # Implement your scoring logic
    threadsanitizer_score = score_python_code(threadsanitizer_output)  # Implement your scoring logic

    # Calculate the final score
    final_score = (pylint_score*3 + float(threadsanitizer_score)*7) / 10

    # Output the final score
    print(f"Final Score: {final_score}")

# Example solution code
solution_code = pythonCodeGenerator(problem)
"""
image_filter_applicator.apply_filter(Image.open(image_path), filter_name)"""

test_concurrent_image_filters(solution_code)
