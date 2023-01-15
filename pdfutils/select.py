import os
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Input argument 'filepath' is missing")

    if len(sys.argv) < 3:
        raise Exception("Input argument 'selection' is missing")

    filepath, ext = os.path.splitext(sys.argv[1])
    selection = eval(sys.argv[2])

    reader = PdfFileReader(filepath + ext)
    writer = PdfFileWriter()

    if isinstance(selection, list):
        pages = [reader.pages[i - 1] for i in selection]
    else:
        pages = reader.pages[selection]

    [writer.addPage(page) for page in pages]

    with open(filepath + " (selection)" + ext, "wb") as f:
        writer.write(f)
