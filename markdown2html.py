#!/usr/bin/python3
"""
This script converts Markdown to HTML.
Supports basic Markdown features like headings and paragraphs.
"""

import sys
import os
import re

def markdown_to_html(md_content):
    """Convert Markdown text to HTML."""
    html_content = []
    lines = md_content.split('\n')
    in_list = False  # Track if we are inside a list
    
    for line in lines:
        if re.match(r'^#{1,6}\s', line):  # Matches Markdown headings
            level = len(line.split(' ')[0])  # Determine the heading level
            content = line[level:].strip()
            html_content.append(f'<h{level}>{content}</h{level}>')
        elif line.strip():  # Any non-empty line is treated as a paragraph
            html_content.append(f'<p>{line.strip()}</p>')

    return '\n'.join(html_content)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_filename = sys.argv[1]
    html_filename = sys.argv[2]

    if not os.path.exists(md_filename):
        print(f"Missing {md_filename}", file=sys.stderr)
        sys.exit(1)
    
    with open(md_filename, 'r') as md_file:
        md_content = md_file.read()

    html_content = markdown_to_html(md_content)

    with open(html_filename, 'w') as html_file:
        html_file.write(html_content)

    print(f"Converted {md_filename} to {html_filename}.")
    sys.exit(0)

if __name__ == "__main__":
    main()
