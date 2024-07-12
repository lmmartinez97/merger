import os
import sys
from docx import Document
import re
from ebooklib import epub

def natural_sort_key(s):
    _nsre = re.compile(r'(\d+)')
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]

def extract_title(file_name):
    return re.sub(r'^\d+\s*-\s*', '', file_name).rsplit('.', 1)[0]

def merge_docx_files_to_epub(folder_path, output_file):
    # Extract the book title from the directory name
    book_title = os.path.basename(folder_path)
    
    # Get a list of all DOCX files in the folder
    docx_files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]
    
    # Sort the files using natural sort based on the numerical prefix
    docx_files.sort(key=natural_sort_key)
    
    # Create an EPUB book
    book = epub.EpubBook()
    book.set_title(book_title)
    
    spine = ['nav']
    toc = []

    for file in docx_files:
        file_path = os.path.join(folder_path, file)
        chapter_title = extract_title(file)
        
        # Read the content of each DOCX file
        doc = Document(file_path)
        content = '\n'.join([p.text for p in doc.paragraphs])
        
        # Create an EPUB chapter
        c = epub.EpubHtml(title=chapter_title, file_name=f'{chapter_title}.xhtml', lang='en')
        c.content = f'<h1>{chapter_title}</h1><p>{content.replace("\n", "<br>")}</p>'
        
        # Add chapter to book
        book.add_item(c)
        spine.append(c)
        toc.append(epub.Link(f'{chapter_title}.xhtml', chapter_title, chapter_title))
    
    # Add table of contents and spine
    book.toc = toc
    book.spine = spine
    
    # Define CSS style
    style = 'BODY { font-family: Arial, sans-serif; }'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    
    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Write to the output file
    epub.write_epub(output_file, book, {})

def main():
    if len(sys.argv) != 3:
        print("Usage: merge-docx <folder_path> <output_file>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = sys.argv[2]
    
    merge_docx_files_to_epub(folder_path, output_file)

if __name__ == "__main__":
    main()
