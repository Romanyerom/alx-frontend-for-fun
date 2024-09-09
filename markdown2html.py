#!/usr/bin/env python3
import sys
import os
import markdown

# Check if the number of arguments is less than 2
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Assign the arguments to variables
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Read the markdown file
try:
    with open(markdown_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

# Exit with success code
sys.exit(0)
