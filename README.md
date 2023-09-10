

# Evaluating AI Multithreading Skills

In the world of software development, the ability to write multithreaded code is becoming increasingly important. Many applications rely on concurrent processing to improve performance and responsiveness. To assess AI's ability to write multithreaded code, we have generated 100 unique problems that require the use of multiple threads. This repository provides descriptions of these problems, their requirements, and test cases.

## Problems

Each problem is presented as a text description and accompanied by a list of requirements. These problems are diverse and cover various aspects of multithreading, including synchronization, parallelism, and thread safety.

## Testing

To evaluate the solutions submitted by AI, we have provided automated Python code for testing. The testing process includes the following steps:

1. **Correctness Testing**: The AI-generated code is tested with a set of inputs to determine if it produces the correct output.

2. **Thread Safety Testing**: We use ThreadSanitizer to analyze the AI-generated code for potential data races and thread safety issues. This ensures that the code can safely run in a multithreaded environment.

3. **Scoring**: The AI-generated code is evaluated based on its correctness and thread safety. A score is assigned to each solution, reflecting its quality and safety.

## Pass Criteria

We have set the following criteria for code qualification:

- The code must pass correctness testing, meaning it produces the correct output for the given inputs.

- The code must achieve a score of 90 or higher. This score is calculated based on correctness and thread safety.

## Repository Structure

- `100problems`: Contains the text descriptions and requirements of the 100 multithreading problems and their automation code. 

- `util`: two Python codes for calculating the scores of the submitted code.

## Getting Started

Simply give the Solution Code you need to assess then run each problem, then you can get whether your code's output is correct and its thread-safety score.
