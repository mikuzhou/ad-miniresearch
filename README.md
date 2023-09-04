Evaluating AI Multithreading Skills

In the world of software development, the ability to write multithreaded code is becoming increasingly important. Many applications rely on concurrent processing to improve performance and responsiveness. To assess AI's ability to write multithreaded code, we have generated 100 unique problems that require the use of multiple threads. This repository provides descriptions of these problems, their requirements, and test cases.

Problems

Each problem is presented as a text description and accompanied by a list of requirements. These problems are diverse and cover various aspects of multithreading, including synchronization, parallelism, and thread safety.

Testing

To evaluate the solutions submitted by AI, we have provided automated Python code for testing. The testing process includes the following steps:

Correctness Testing: The AI-generated code is tested with a set of inputs to determine if it produces the correct output.
Thread Safety Testing: We use ThreadSanitizer to analyze the AI-generated code for potential data races and thread safety issues. This ensures that the code can safely run in a multithreaded environment.
Scoring: The AI-generated code is evaluated based on its correctness and thread safety. A score is assigned to each solution, reflecting its quality and safety.
Pass Criteria

We have set the following criteria for code qualification:

The code must pass correctness testing, meaning it produces the correct output for the given inputs.
The code must achieve a score of 90 or higher. This score is calculated based on correctness and thread safety.
Repository Structure

problems: Contains the text descriptions of the 100 multithreading problems.
requirements: Lists the specific requirements for each problem.
tests: Includes the test cases and testing scripts for evaluating the AI-generated code.
score_calculator.py: A Python script for calculating the scores of the submitted code.
Getting Started

To begin, explore the problems directory to view the problem descriptions and their requirements. AI-generated code can be tested using the provided test cases in the tests directory. The score_calculator.py script calculates the final scores.

Contributions

Contributions and improvements to the problem descriptions, testing scripts, or any aspect of this evaluation process are welcome. Please open issues or pull requests to suggest changes.
