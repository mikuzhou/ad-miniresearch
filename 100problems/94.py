import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
# Problem 90: Concurrent Email Sending
#
problem = "Description: Create a program to concurrently send emails to multiple recipients using different email servers.\
\
Requirements:\
\
Implement an email sending system that allows multiple emails to be sent concurrently to various recipients.\
Ensure that emails are sent correctly and concurrently.\
Test Set:\
\
Provide a list of email messages, recipient addresses, and email servers.\
Execute email sending functions concurrently.\
Verify that emails are sent correctly."
class EmailSender:
    def __init__(self):
        self.sent_emails = {}
        self.lock = threading.Lock()

    def send_email(self, recipient, message, email_server):
        with self.lock:
            # Simulate sending an email
            sent_email = f"Sent to {recipient} via {email_server}: {message}"
            self.sent_emails[recipient] = sent_email

def test_concurrent_email_sending(solution_code):
    email_requests = [
        ("user1@example.com", "Hello User 1", "smtp.example.com"),
        ("user2@example.com", "Greetings User 2", "smtp.example.net"),
        ("user3@example.com", "Hi User 3", "smtp.example.org"),
    ]
    email_sender = EmailSender()

    # Execute the provided solution_code in separate threads
    def execute_solution(recipient, message, email_server):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for recipient, message, email_server in email_requests:
            executor.submit(execute_solution, recipient, message, email_server)

    # Verify the correctness of email sending
    for recipient, message, email_server in email_requests:
        # assert recipient in email_sender.sent_emails, f"Email not sent to {recipient}"
        # assert email_sender.sent_emails[recipient] == f"Sent to {recipient} via {email_server}: {message}", f"Incorrect email sent to {recipient}"

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
email_sender.send_email(recipient, message, email_server)
"""

test_concurrent_email_sending(solution_code)
