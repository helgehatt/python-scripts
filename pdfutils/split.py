import os
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Input argument 'filepath' is missing")

    filepath, ext = os.path.splitext(sys.argv[1])

    reader = PdfFileReader(filepath + ext)

    for idx, page in enumerate(reader.pages, 1):
        writer = PdfFileWriter()
        writer.addPage(page)

        with open(filepath + f" ({idx})" + ext, "wb") as f:
            writer.write(f)
