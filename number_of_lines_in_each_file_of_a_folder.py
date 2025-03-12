import os
import csv

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

def export_file_line_counts_to_csv(folder_path, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Filename', 'Location', 'Line Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # Walk through the directory and subdirectories
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.py'):  # Check if the file is a Python file
                    file_path = os.path.join(root, file)
                    line_count = count_lines_in_file(file_path)
                    writer.writerow({'Filename': file, 'Location': file_path, 'Line Count': line_count})

# Example usage
folder_path = '/Users/hrs/Documents/forseeit-predictive-monitoring/healthscore-dev'  # Replace with the path to your folder
output_csv = 'python_files_line_counts.csv'  # Output CSV file name
export_file_line_counts_to_csv(folder_path, output_csv)

print(f"CSV export completed: {output_csv}")
