import os

def convert_soft_breaks_to_spaces(input_str):
    lines = input_str.split('\n')
    for i, line in enumerate(lines):
        if not line.endswith('  '):
            lines[i] = line.rstrip() + '  '
    return '\n'.join(lines)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the output directory if it doesn't exist
output_dir = os.path.join(script_dir, "New Files")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all files and directories in the script directory
for root, dirs, files in os.walk(script_dir):
    for file in files:
        if file.endswith(".md"):
            # Read the input file
            with open(os.path.join(root, file), 'r') as f:
                input_str = f.read()
            # Convert soft breaks to hard breaks while ensuring there are always exactly 2 spaces at the end of each line
            output_str = convert_soft_breaks_to_spaces(input_str)
            # Get the relative directory path of the input file
            rel_dir = os.path.relpath(root, script_dir)
            # Create the output directory for the file
            output_subdir = os.path.join(output_dir, rel_dir)
            if not os.path.exists(output_subdir):
                os.makedirs(output_subdir)
            # Write the output file to the output directory with the same filename as the input file
            output_file = os.path.join(output_subdir, file)
            with open(output_file, 'w') as f:
                f.write(output_str)
