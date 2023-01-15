import os

folder = "D:/Backup/Sara-MacBook (2015-2016)"

files = [
    os.path.join(dp, f)
    for dp, ds, fs in os.walk(folder)
    for f in fs
    if f.endswith(".psd")
]

print(*files, sep="\n")
