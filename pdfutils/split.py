import argparse
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def split(src: Path, dst: Path):
    reader = PdfReader(src)
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        writer.write(dst.with_stem(f"{dst.stem} ({i + 1})"))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=Path)
    parser.add_argument("--filename", "-f", type=Path)
    parser.add_argument("--dryrun", "-n", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    filename = args.filename or args.filepath

    if args.dryrun:
        print(f"Split '{args.filepath}' and save as '{filename} (page number)'")
    else:
        split(args.filepath, filename)
