import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 14: Concurrent Chat Application
#
# Description: Develop a chat application where multiple users can send and receive messages concurrently.
#
# Requirements:
#
# Implement a chat application that allows multiple users to send and receive messages concurrently.
# Ensure that messages are sent and received correctly and concurrently.
# Test Set:
#
# Simulate multiple users sending and receiving messages concurrently.
# Verify that messages are correctly sent and received.
class ChatApplication:
    def __init__(self):
        self.messages = []
        self.lock = threading.Lock()

    def send_message(self, user, message):
        with self.lock:
            self.messages.append(f"{user}: {message}")

    def receive_messages(self):
        with self.lock:
            return self.messages

def test_concurrent_chat_application(solution_code):
    chat_app = ChatApplication()

    # Execute the provided solution_code in separate threads to send messages
    def send_messages(user, messages):
        for message in messages:
            exec(solution_code)

    users = ["User1", "User2", "User3"]
    messages = [
        ["Hello", "How are you?"],
        ["Hi", "I'm good, thanks!"],
        ["Hey there!"],
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for user, message_set in zip(users, messages):
            executor.submit(send_messages, user, message_set)

    # Retrieve and verify received messages
    time.sleep(1)  # Give threads some time to send messages
    received_messages = chat_app.receive_messages()
    expected_messages = ["User1: Hello", "User1: How are you?", "User2: Hi", "User2: I'm good, thanks!", "User3: Hey there!"]
    assert all(message in received_messages for message in expected_messages), "Incorrect message reception"

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
chat_app.send_message(user, message)
"""

test_concurrent_chat_application(solution_code)
