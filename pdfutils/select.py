import argparse
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def select(src: Path, dst: Path, *selection: int):
    reader = PdfReader(src)
    writer = PdfWriter()
    for i in selection:
        writer.add_page(reader.pages[i - 1])
    writer.write(dst)


if __name__ == "__main__":

    def selection_format(input: str):
        """Converts the input to a valid selection.

        >>> selection_format("1")
        [1]

        >>> selection_format("1,4,5,7")
        [1, 4, 5, 7]

        >>> selection_format("1-3,4-6,7")
        [1, 2, 3, 4, 5, 6, 7]

        """

        def closure():
            for arg in input.split(","):
                if "-" in arg:
                    a, b = arg.split("-")
                    for i in range(int(a), int(b) + 1):
                        yield i
                else:
                    yield int(arg)

        return list(closure())

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=Path)
    parser.add_argument("selection", type=selection_format)
    parser.add_argument("--filename", "-f", type=Path)
    parser.add_argument("--dryrun", "-n", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    filename = args.filename or args.filepath.with_stem(
        args.filepath.stem + ".selection"
    )

    if args.dryrun:
        print(
            f"Select pages {args.selection} from '{args.filepath}' and save as '{filename}'"
        )
    else:
        select(args.filepath, filename, *args.selection)

    # reader = PdfFileReader(filepath + ext)
    # writer = PdfFileWriter()

    # if isinstance(selection, list):
    #     pages = [reader.pages[i - 1] for i in selection]
    # else:
    #     pages = reader.pages[selection]

    # [writer.addPage(page) for page in pages]

    # with open(filepath + " (selection)" + ext, "wb") as f:
    #     writer.write(f)
