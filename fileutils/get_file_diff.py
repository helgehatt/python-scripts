import os

folder1 = "H:/Other computers/My MacBook Pro/Pictures"
folder2 = "D:/Backup/Sara-MacBook Pro (2017-2022)/Pictures"


def get_files(folder: str):
    return [
        os.path.relpath(os.path.join(dp, f), folder)
        for dp, ds, fs in os.walk(folder)
        for f in fs
    ]


files1 = get_files(folder1)
files2 = get_files(folder2)

len(set(files1) - set(files2))
len(set(files2) - set(files1))
