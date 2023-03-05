import argparse
import glob
from pathlib import Path

from PyPDF2 import PdfMerger


def merge(filename: str, *files: str):
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    merger.write(filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=str)
    parser.add_argument("--filename", "-f", type=Path)
    parser.add_argument("--dryrun", "-n", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    files = [Path(f) for file in args.files for f in glob.glob(file)]

    filename = args.filename or files[0].with_stem(files[0].stem + ".merged")

    if args.dryrun:
        print(f"Merge the following files into '{filename}':", *files, sep="\n")
    else:
        merge(filename, *files)
