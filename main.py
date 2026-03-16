import csv
import os

# Define the parent directory where your project resides
project_dir = os.path.dirname(os.path.abspath(__file__))

# Define the subdirectory containing the sample files
subdir = 'sample_data'

# Combine the project and subdirectories to get the full path of the 
sample directory
sample_path = os.path.join(project_dir, subdir)

# Specify the name of the file you want to read
filename = 'your_dataset.csv'

# Construct the full path of the file
file_path = os.path.join(sample_path, filename)

# Open the file using a suitable mode (e.g., 'r' for reading)
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Iterate through rows and process data as needed
    for row in reader:
        print(row)