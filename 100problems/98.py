import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import time
# Problem 94: Concurrent Chat Application
#
problem = "Description: Create a concurrent chat application that allows multiple users to send and receive messages in real-time.\
\
Requirements:\
\
Implement a chat application that supports multiple users communicating concurrently.\
Ensure that messages are delivered correctly and in real-time to the intended recipients.\
Test Set:\
\
Simulate multiple users sending messages concurrently.\
Verify that messages are correctly delivered to the intended recipients in real-time."

class ChatApplication:
    def __init__(self):
        self.messages = []
        self.lock = threading.Lock()

    def send_message(self, sender, recipient, message):
        with self.lock:
            # Simulate sending a message
            self.messages.append((sender, recipient, message))

    def get_messages(self, user):
        with self.lock:
            # Simulate retrieving messages for a user
            user_messages = [(sender, recipient, message) for sender, recipient, message in self.messages if
                             recipient == user]
            return user_messages


def test_concurrent_chat_application(solution_code):
    chat_app = ChatApplication()

    # Execute the provided solution_code in separate threads
    def execute_solution(sender, recipient, message):
        exec(solution_code)

    users = ["User1", "User2", "User3"]
    chat_threads = []

    for i in range(len(users)):
        for j in range(len(users)):
            if i != j:
                chat_threads.append(threading.Thread(target=execute_solution,
                                                     args=(users[i], users[j], f"Hello from {users[i]} to {users[j]}")))

    for thread in chat_threads:
        thread.start()

    for thread in chat_threads:
        thread.join()

    # Verify the correctness of message delivery
    for user in users:
        messages = chat_app.get_messages(user)
        # for sender, recipient, message in messages:
        # assert user == recipient, f"Message delivered to the wrong recipient: {message}"

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
chat_app.send_message(sender, recipient, message)
"""

test_concurrent_chat_application(solution_code)
