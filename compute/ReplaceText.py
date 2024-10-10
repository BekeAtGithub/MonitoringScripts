# Define the input file path and the output file path
input_file = 'C:\File\Input\Path'   # Replace with your actual file name
output_file = 'C:\File\Output\Path' # This will save the modified content to a new file

# Open the input file, read the content, and perform the replacement
with open(input_file, 'r') as file:
    content = file.read()

# Replace all backticks ` with hyphen -
modified_content = content.replace('`', '-')

# Write the modified content to the output file
with open(output_file, 'w') as file:
    file.write(modified_content)

print(f"All backticks ` have been replaced with hyphens - in '{output_file}'.")
