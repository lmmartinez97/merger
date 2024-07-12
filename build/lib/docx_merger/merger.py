import os
import sys
from docx import Document
import re

def natural_sort_key(s):
    _nsre = re.compile('([0-9]+)')
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]

def merge_docx_files(folder_path, output_file):
    # Get a list of all DOCX files in the folder
    docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]
    
    # Sort the files using natural sort
    docx_files.sort(key=natural_sort_key)

    # Create a new Document
    merged_document = Document()

    for file in docx_files:
        file_path = os.path.join(folder_path, file)
        sub_doc = Document(file_path)
        # Add a page break after each document except the last one
        for element in sub_doc.element.body:
            merged_document.element.body.append(element)
        merged_document.add_page_break()

    # Remove the last page break
    if len(merged_document.element.body) > 0 and merged_document.element.body[-1].tag.endswith('sectPr'):
        merged_document.element.body[-1].getparent().remove(merged_document.element.body[-1])

    # Save the merged document
    merged_document.save(output_file)

def main():
    if len(sys.argv) != 3:
        print("Usage: merge-docx <folder_path> <output_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = sys.argv[2]
    
    merge_docx_files(folder_path, output_file)

if __name__ == "__main__":
    main()

