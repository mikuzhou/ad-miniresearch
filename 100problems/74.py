import threading
from util.code_generate import pythonCodeGenerator
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import random
# Problem 69: Concurrent Payment Processing
#
problem = "Description: Develop a program to concurrently process payments from multiple customers.\
\
Requirements:\
\
Implement a payment processing system that allows multiple payments to be processed concurrently.\
Ensure that payments are processed correctly and concurrently.\
Test Set:\
\
Provide a list of customer payments and payment processing tasks.\
Execute payment processing functions concurrently.\
Verify that all payments are processed successfully."
class PaymentProcessor:
    def __init__(self):
        self.processed_payments = []
        self.lock = threading.Lock()

    def process_payment(self, customer_name, amount):
        with self.lock:
            # Simulate payment processing with random success or failure
            success = random.choice([True, False])
            if success:
                self.processed_payments.append((customer_name, amount))
            else:
                print(f"Payment failed for {customer_name}: ${amount}")

def test_concurrent_payment_processing(solution_code):
    payments_and_customers = [
        ("Customer1", 50.0),
        ("Customer2", 100.0),
        ("Customer3", 75.0),
    ]
    payment_processor = PaymentProcessor()

    # Execute the provided solution_code in separate threads
    def execute_solution(customer_name, amount):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for customer_name, amount in payments_and_customers:
            executor.submit(execute_solution, customer_name, amount)

    # Verify the correctness of payment processing
    for customer_name, amount in payments_and_customers:
        assert (customer_name, amount) in payment_processor.processed_payments, f"Incorrect payment processing: {customer_name}, ${amount}"

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
solution_code = pythonCodeGenerator(problem); """
payment_processor.process_payment(customer_name, amount)
"""

test_concurrent_payment_processing(solution_code)
