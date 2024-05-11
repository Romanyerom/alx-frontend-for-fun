#!/usr/bin/python3
"""
Convert Markdown to HTML.
Supports headings, paragraphs, lists, and bold text.
"""

import sys
import os
import re

def markdown_to_html(md_content):
    """Convert Markdown text to HTML."""
    html_content = []
    lines = md_content.split('\n')
    in_list = False
    
    for line in lines:
        if re.match(r'^#{1,6}\s', line):
            level = len(line.split(' ')[0])  # Count number of '#'
            content = line[level:].strip()
            html_content.append(f'<h{level}>{content}</h{level}>')
        elif re.match(r'^[\*\-\+]\s', line):
            content = line[2:].strip()
            if not in_list:
                html_content.append('<ul>')
                in_list = True
            html_content.append(f'<li>{content}</li>')
        elif in_list:
            html_content.append('</ul>')
            in_list = False
        elif '**' in line or '__' in line:
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
            html_content.append(f'<p>{line}</p>')
        elif line.strip():
            html_content.append(f'<p>{line.strip()}</p>')
    
    if in_list:
        html_content.append('</ul>')

    return '\n'.join(html_content)

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    md_filename = sys.argv[1]
    html_filename = sys.argv[2]

    if not os.path.exists(md_filename):
        print(f"Missing {md_filename}", file=sys.stderr)
        sys.exit(1)
    
    with open(md_filename, 'r') as f:
        md_content = f.read()

    html_content = markdown_to_html(md_content)

    with open(html_filename, 'w') as f:
        f.write(html_content)

    print(f"Converted {md_filename} to {html_filename}.")
    sys.exit(0)

if __name__ == "__main__":
    main()
