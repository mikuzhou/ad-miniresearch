import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import requests
# Problem 17: Concurrent Image Uploads
#
problem = "Description: Create a program that uploads images concurrently to a server.\
\
Requirements:\
\
Implement an image upload system that allows multiple images to be uploaded concurrently to a server.\
Ensure that images are uploaded correctly and concurrently.\
Test Set:    image_files = [\"image1.jpg\", \"image2.jpg\", \"image3.jpg\"]\
    server_url = \"http://example.com/upload\"\
\
Provide a set of image files for upload.\
Execute image upload functions concurrently to a server.\
Verify that all images are uploaded correctly."
class ImageUploader:
    def __init__(self, server_url):
        self.server_url = server_url
        self.uploaded_images = []
        self.lock = threading.Lock()

    def upload_image(self, image_file):
        with self.lock:
            response = requests.post(self.server_url, files={'image': open(image_file, 'rb')})
            if response.status_code == 200:
                self.uploaded_images.append(image_file)
            else:
                return False
            return True

def test_concurrent_image_uploads(solution_code):
    image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]
    server_url = "http://example.com/upload"
    image_uploader = ImageUploader(server_url)

    # Execute the provided solution_code in separate threads
    def execute_solution(image_file):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for image_file in image_files:
            executor.submit(execute_solution, image_file)

    # Verify the correctness of uploaded images
    # assert all(image_file in image_uploader.uploaded_images for image_file in image_files), "Incorrect image uploads"

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
if image_uploader.upload_image(image_file):
    # Process the uploaded image as needed
    pass
"""

test_concurrent_image_uploads(solution_code)
