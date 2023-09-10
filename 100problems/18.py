import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Problem 18: Concurrent Email Sending
#
problem = "Description: Build a program that sends emails concurrently to a list of recipients.\
\
Requirements:\
\
Implement an email sending system that allows multiple emails to be sent concurrently.\
Ensure that emails are sent correctly and concurrently.\
Test Set:\
\
Provide a list of email addresses as recipients.\
Execute email sending functions concurrently.\
Verify that all emails are sent correctly."
class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.sent_emails = []
        self.lock = threading.Lock()

    def send_email(self, recipient_email, subject, message):
        with self.lock:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            try:
                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
                server.close()
                self.sent_emails.append(recipient_email)
                return True
            except Exception as e:
                print(f"Email sending failed: {e}")
                return False


def test_concurrent_email_sending(solution_code):
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "sender@example.com"
    sender_password = "password"
    recipient_emails = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
    email_sender = EmailSender(smtp_server, smtp_port, sender_email, sender_password)

    # Execute the provided solution_code in separate threads
    def execute_solution(recipient_email):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for recipient_email in recipient_emails:
            executor.submit
