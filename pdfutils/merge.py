import glob
import os
import sys

from PyPDF2 import PdfFileMerger

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Input argument 'filepath' is missing")

    filepath = sys.argv[1]
    files = glob.glob(filepath)
    files = list(sorted(files, key=len))

    merger = PdfFileMerger()
    for f in files:
        merger.append(f)

    filename, ext = os.path.splitext(files[0])
    merger.write(f"{filename} (merged){ext}")
