# PDF Bookmark Renamer

A simple command-line tool to view and rename PDF bookmarks interactively.

## Requirements

- Python 3.6+
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) (`fitz` module)

Install the requirements with:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python PDFBookmarkRenamer.py <input.pdf>
```

Example:

```bash
python PDFBookmarkRenamer.py mydocument.pdf
```

Interactive example:

```
1: Introduction (Page: 1)
2: Chapter 1 (Page: 5)
...

Bookmark Number (or 'done'): 2
New name for 'Chapter 1': Getting Started
Bookmark Number (or 'done'): done
```

New file saved as:

```
mydocument_renamed.pdf
```
