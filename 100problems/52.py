import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
# Problem 44: Concurrent Chat Application
#
# Description: Build a concurrent chat application where multiple users can send and receive messages.
#
# Requirements:
#
# Implement a chat application that allows multiple users to send and receive messages concurrently.
# Ensure that messages are sent and received correctly and concurrently.
# Test Set:
#
# Simulate multiple users sending and receiving messages concurrently.
# Verify that all messages are delivered correctly.
class ChatApplication:
    def __init__(self):
        self.received_messages = []
        self.lock = threading.Lock()

    def send_message(self, sender, receiver, message):
        with self.lock:
            # Implement message sending logic here
            self.received_messages.append((sender, receiver, message))

def test_concurrent_chat_application(solution_code):
    users = ["User1", "User2", "User3"]
    messages = [
        ("User1", "User2", "Hello, User2!"),
        ("User2", "User3", "Hi there, User3!"),
        ("User3", "User1", "Hey, User1!"),
    ]
    chat_application = ChatApplication()

    # Execute the provided solution_code in separate threads
    def execute_solution(sender, receiver, message):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for sender, receiver, message in messages:
            executor.submit(execute_solution, sender, receiver, message)

    # Verify the correctness of message delivery
    for sender, receiver, message in messages:
        assert (sender, receiver, message) in chat_application.received_messages, "Incorrect message delivery"

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
chat_application.send_message(sender, receiver, message)
"""

test_concurrent_chat_application(solution_code)
