import os
import fnmatch

# Define the file patterns to look for
react_patterns = ['*.js', '*.jsx', '*.ts', '*.tsx']
html_patterns = ['*.html']
style_patterns = ['*.css', '*.scss', '*.sass']

# Define the directory to start from
root_dir = 'C:/Users/HP/Desktop/FSWD/Projects/actodo'  # Change this to your project's root directory

# Define the output file
output_file = 'project_code.txt'

# Function to check if the file matches any of the patterns
def matches_pattern(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

# Open the output file
with open(output_file, 'w') as outfile:
    # Walk through the directory
    for root, dirs, files in os.walk(root_dir):
        # Skip node_modules directory
        dirs[:] = [d for d in dirs if d != 'node_modules']
        
        for file in files:
            if matches_pattern(file, react_patterns + html_patterns + style_patterns):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(f"--- {file_path} ---\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n")

print(f"Extraction complete. All code has been written to {output_file}")
