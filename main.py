
import os
import subprocess
import json

def execute_python_files_in_folder_and_get_scores(folder_path):
    total_score = 0.0  # Variable to hold the total score
    num_files = 0    # Variable to count the number of executed Python files
    
    # Iterate over all files in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):  # Process only Python files
                num_files += 1  # Increment the file counter
                file_path = os.path.join(root, file)
                print(f"Executing {file_path}...")
                
                # Run the Python file and capture the output
                try:
                    result = subprocess.run(["python", file_path], check=True, text=True, capture_output=True)
                    output = result.stdout.strip()  # Get the stdout output and strip any extra whitespace
                    
                    # Assume that the score is printed as the last line of the output
                    score_line = output.split("\n")[-1]
                    score = float(score_line.split()[-1])  # Assume the score is the last word in the last line
                    total_score += score  # Add the score to the total score
                    
                    print(f"Score from {file}: {score}")
                except Exception as e:
                    print(f"An error occurred while executing {file_path}: {e}")

    
    return total_score, num_files

# Execute all Python files in the '100problems' folder and get the total score
folder_path = os.path.join(os.getcwd(), '100problems')
total_score, num_files = execute_python_files_in_folder_and_get_scores(folder_path)

# Print the total score
print(f"Total Score: {total_score}/{num_files*100}")

# Save the total score to 'output.json'
output = {"output": f"{total_score/num_files}/{num_files*100}"}
with open("output.json", "w") as json_file:
    json.dump(output, json_file)
