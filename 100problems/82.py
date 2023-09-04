import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import smtplib
# Problem 77: Concurrent Email Sending
#
# Description: Develop a program to concurrently send emails to a list of recipients.
#
# Requirements:
#
# Implement an email sending system that allows multiple emails to be sent concurrently to different recipients.
# Ensure that emails are sent correctly and concurrently.
# Test Set:
#
# Provide a list of recipient email addresses and email content.
# Execute email sending functions concurrently.
# Verify that emails are successfully sent to all recipients.
class EmailSender:
    def __init__(self):
        self.sent_emails = []
        self.lock = threading.Lock()

    def send_email(self, recipient_email, subject, message):
        with self.lock:
            # Simulate sending email
            try:
                smtp_server = smtplib.SMTP('smtp.example.com')
                smtp_server.sendmail('sender@example.com', recipient_email, f"Subject: {subject}\n\n{message}")
                smtp_server.quit()
                self.sent_emails.append(recipient_email)
            except Exception as e:
                print(f"Failed to send email to {recipient_email}: {str(e)}")

def test_concurrent_email_sending(solution_code):
    recipients_and_emails = [
        ("recipient1@example.com", "Important Update", "Please review the attached document."),
        ("recipient2@example.com", "Hello", "Greetings from our team!"),
        ("recipient3@example.com", "Meeting Invitation", "You are invited to our upcoming meeting."),
    ]
    email_sender = EmailSender()

    # Execute the provided solution_code in separate threads
    def execute_solution(recipient_email, subject, message):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for recipient_email, subject, message in recipients_and_emails:
            executor.submit(execute_solution, recipient_email, subject, message)

    # Verify the correctness of email sending
    for recipient_email, _, _ in recipients_and_emails:
        assert recipient_email in email_sender.sent_emails, f"Email not sent to: {recipient_email}"

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
email_sender.send_email(recipient_email, subject, message)
"""

test_concurrent_email_sending(solution_code)
