import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
from collections import defaultdict
# Problem 11: Concurrent Order Processing
#
# Description: Create a program to process orders concurrently from multiple customers.
#
# Requirements:
#
# Implement an order processing system that allows multiple customer orders to be processed concurrently.
# Ensure that orders are processed correctly and concurrently, and that stock is updated accurately.
# Test Set:
#
# Define a set of customer orders, each with a list of items and quantities.
# Execute order processing functions concurrently, deducting items from stock.
# Verify that orders are processed correctly and stock is updated accurately.
class OrderProcessor:
    def __init__(self):
        self.stock = defaultdict(int)
        self.lock = threading.Lock()

    def process_order(self, order):
        with self.lock:
            for item, quantity in order.items():
                if self.stock[item] >= quantity:
                    self.stock[item] -= quantity
                else:
                    return False
            return True

def test_concurrent_order_processing(solution_code):
    customer_orders = [
        {"item1": 3, "item2": 2},
        {"item2": 4, "item3": 1},
        {"item1": 1, "item3": 2},
    ]
    order_processor = OrderProcessor()

    # Execute the provided solution_code in separate threads
    def execute_solution(order):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for order in customer_orders:
            executor.submit(execute_solution, order)

    # Verify the correctness of order processing and stock update
    assert all(order_processor.process_order(order) for order in customer_orders), "Incorrect order processing"

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
if order_processor.process_order(order):
    # Update stock
    for item, quantity in order.items():
        order_processor.stock[item] -= quantity
"""

test_concurrent_order_processing(solution_code)
