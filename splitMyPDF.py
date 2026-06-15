from pathlib import Path
import sys
import re

from pypdf import PdfReader, PdfWriter

DEFAULT_FILE = "input.pdf"
OUTPUT_DIR = "split"


def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip()


def get_top_level_bookmarks(reader):
    bookmarks = []

    try:
        outline = reader.outline
    except Exception:
        return bookmarks

    for item in outline:
        if isinstance(item, list):
            continue

        try:
            bookmarks.append({
                "title": item.title,
                "page": reader.get_destination_page_number(item)
            })
        except Exception:
            pass

    return bookmarks


def split_pdf_by_bookmarks(pdf_path):
    reader = PdfReader(pdf_path)

    bookmarks = get_top_level_bookmarks(reader)

    if not bookmarks:
        print("Tidak ditemukan bookmark level 1.")
        return

    output_dir = Path(pdf_path).parent / OUTPUT_DIR
    output_dir.mkdir(exist_ok=True)

    total_pages = len(reader.pages)

    for idx, bookmark in enumerate(bookmarks):
        start_page = bookmark["page"]

        if idx < len(bookmarks) - 1:
            end_page = bookmarks[idx + 1]["page"]
        else:
            end_page = total_pages

        writer = PdfWriter()

        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        filename = sanitize_filename(bookmark["title"])

        if not filename:
            filename = f"part_{idx+1}"

        output_file = output_dir / f"{filename}.pdf"

        with open(output_file, "wb") as f:
            writer.write(f)

        print(f"[OK] {output_file.name}")

    print("\nSelesai.")


def main():

    # MODE 1: Drag & Drop
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]

    # MODE 2: Double Click
    else:
        exe_dir = Path(sys.executable).parent if getattr(
            sys,
            "frozen",
            False
        ) else Path(__file__).parent

        pdf_file = exe_dir / DEFAULT_FILE

        if not pdf_file.exists():
            print(f"ERROR: {DEFAULT_FILE} tidak ditemukan.\n")
            print("Cara penggunaan:")
            print(f"1. Letakkan '{DEFAULT_FILE}' di folder yang sama dengan EXE")
            print("ATAU")
            print("2. Drag & drop file PDF ke EXE")
            input("\nTekan Enter untuk keluar...")
            return

    try:
        split_pdf_by_bookmarks(str(pdf_file))
    except Exception as e:
        print(f"\nERROR: {e}")

    input("\nTekan Enter untuk keluar...")


if __name__ == "__main__":
    main()