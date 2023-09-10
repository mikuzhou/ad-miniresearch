import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 24: Concurrent Social Media Posts
#
problem = "Description: Develop a program for posting social media updates concurrently.\
\
Requirements:\
\
Implement a social media posting system that allows multiple users to post updates concurrently.\
Ensure that updates are posted correctly and concurrently.\
Test Set:\
\
Simulate multiple users posting updates concurrently.\
Verify that the updates are posted correctly."
class SocialMediaPlatform:
    def __init__(self):
        self.posts = []
        self.lock = threading.Lock()

    def post_update(self, user, update):
        with self.lock:
            self.posts.append(f"{user}: {update}")

    def get_updates(self):
        with self.lock:
            return self.posts

def test_concurrent_social_media_posts(solution_code):
    social_media = SocialMediaPlatform()

    # Execute the provided solution_code in separate threads to post updates
    def post_updates(user, updates):
        for update in updates:
            exec(solution_code)

    users = ["User1", "User2", "User3"]
    updates = [
        ["Update 1", "Update 2"],
        ["Hello", "Hi"],
        ["Good morning!"],
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for user, update_set in zip(users, updates):
            executor.submit(post_updates, user, update_set)

    # Retrieve and verify posted updates
    time.sleep(1)  # Give threads some time to post updates
    posted_updates = social_media.get_updates()
    expected_updates = ["User1: Update 1", "User1: Update 2", "User2: Hello", "User2: Hi", "User3: Good morning!"]
    # assert all(update in posted_updates for update in expected_updates), "Incorrect update posting"

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
social_media.post_update(user, update)
"""

test_concurrent_social_media_posts(solution_code)
