import threading
import concurrent.futures
import subprocess
from util.pylint_score import extract_pylint_score
from util.threadsanitizer_score import score_python_code
import requests
from bs4 import BeautifulSoup
# Problem 5: Concurrent Web Scraping
#
# Description: Build a program that scrapes information from multiple web pages concurrently.
#
# Requirements:
#
# Implement a function to scrape web pages concurrently.
# Allow multiple threads to scrape web pages concurrently.
# Ensure accurate web scraping and thread-safety.
# Test Set:
#
# Scrape information from multiple web pages concurrently and return the total number of words found.
# Automated Testing Python Code (Simplified):
class WebScraper:
    def __init__(self):
        self.total_words = 0
        self.lock = threading.Lock()

    def scrape_web_page(self, url):
        with self.lock:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            words = soup.get_text().split()
            self.total_words += len(words)

def test_concurrent_web_scraping(solution_code):
    urls = ["http://website1.com", "http://website2.com", "http://website3.com"]
    web_scraper = WebScraper()

    # Execute the provided solution_code in separate threads
    def execute_solution(url):
        exec(solution_code)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(execute_solution, urls)

    # Test correctness
    expected_total_words = sum(len(BeautifulSoup(requests.get(url).text, "html.parser").get_text().split()) for url in urls)
    assert web_scraper.total_words == expected_total_words, "Incorrect total words"

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
web_scraper = WebScraper()
url = "http://website1.com"
web_scraper.scrape_web_page(url)
"""

test_concurrent_web_scraping(solution_code)
