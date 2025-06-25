import fitz #python3 -m pip install -r requirements.tx
import os
import sys


def rename_bookmarks(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()

    if not toc:
        print("No bookmarks found in this PDF.")
        return

    print("\nCurrent Bookmarks:\n")
    for i, (level, title, page) in enumerate(toc):
        indent = "  " * (level - 1)
        print(f"{i + 1}: {indent}{title} (Page: {page})")

    rename_map = {}

    print("\nType the number of the bookmark you want to rename.")
    print("Then type the new name (can include spaces).")
    print("Type 'done' to finish.\n")

    while True:
        selection = input("Bookmark Number (or 'done'): ").strip()
        if selection.lower() == "done":
            break
        if not selection.isdigit():
            print("Please enter a valid number.")
            continue
        index = int(selection) - 1
        if index < 0 or index >= len(toc):
            print("Invalid bookmark number.")
            continue

        old_title = toc[index][1]
        new_title = input(f"New name for '{old_title}': ").strip()
        rename_map[old_title] = new_title

    if not rename_map:
        print("No changes made.")
        return

    new_toc = []
    for level, title, page in toc:
        new_title = rename_map.get(title, title)
        new_toc.append([level, new_title, page])

    doc.set_toc(new_toc)

    base, ext = os.path.splitext(pdf_path)
    output_path = f"{base}_renamed{ext}"
    doc.save(output_path)
    print(f"\nSaved updated PDF as: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python PDFBookmarkRenamer.py <input.pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    rename_bookmarks(pdf_path)
