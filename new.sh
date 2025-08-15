#!/bin/bash

# Project Euler Folder Generator
# This script creates a new folder structure similar to existing Project Euler problems

echo "Project Euler Folder Generator"
echo "=============================="
echo

# Ask for folder name
read -p "Enter the folder name (e.g., '032newfoldername'): " folder_name

# Validate input
if [ -z "$folder_name" ]; then
    echo "Error: Folder name cannot be empty!"
    exit 1
fi

# Check if folder already exists
if [ -d "$folder_name" ]; then
    echo "Error: Folder '$folder_name' already exists!"
    exit 1
fi

# Create the folder
echo "Creating folder: $folder_name"
mkdir "$folder_name"

# Create main.py with basic template
echo "Creating main.py..."
cat > "$folder_name/main.py" << 'EOF'
#!/usr/bin/env python3

def main():
    user_input = input("Give me your input: ")
    
    result = process_input(user_input)
    
    print(f"The result is: {result}")


def process_input(input_value):
    return input_value


if __name__ == "__main__":
    main()
EOF

# Make the Python file executable
chmod +x "$folder_name/main.py"
