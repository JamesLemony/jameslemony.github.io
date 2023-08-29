import os

def convert_soft_breaks_to_spaces(input_str):
    lines = input_str.split('\n')
    for i, line in enumerate(lines):
        if line.strip() and not line.endswith('  '):
            lines[i] = line.rstrip() + '  '
    return '\n'.join(lines)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through all files and directories in the "docs" directory
docs_dir = os.path.join(script_dir, "content")
for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            # Read the input file
            input_file = os.path.join(root, file)
            with open(input_file, 'r') as f:
                input_str = f.read()
            # Convert soft breaks to hard breaks while ensuring there are always exactly 2 spaces at the end of each line and removing "%3E" character at the start of a line
            output_str = convert_soft_breaks_to_spaces(input_str)
            # Write the output file to the input file with the same filename
            with open(input_file, 'w') as f:
                f.write(output_str)