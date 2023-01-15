import os
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise Exception("Input argument 'filepath' is missing")

    filepath, ext = os.path.splitext(sys.argv[1])

    reader = PdfFileReader(filepath + ext)
    writer = PdfFileWriter()

    for page in reader.pages:
        writer.addPage(page.rotateClockwise(90))

    with open(filepath + " (rotated)" + ext, "wb") as f:
        writer.write(f)
