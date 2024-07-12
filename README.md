# docx_merger

A simple Python package to merge multiple DOCX files into a single EPUB file with chapter titles.

Expects the following folder structure:

```bash
Book Title
├── 00 - Title of Chapter 0.docx
├── 01 - Title of Chapter 1.docx
├── 02 - Title of Chapter 2.docx
├── 03 - Title of Chapter 3.docx
.
.
.
```

## Usage

```bash
merge-docx /path/to/your/folder output_file.epub
```

## Installation

```sh
pip install .
```