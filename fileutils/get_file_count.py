import os

folder1 = "H:/Other computers/My Computer/Pictures"
folder2 = "D:/Backup/Sara-MacBook (2015-2016)/Pictures"


def get_file_count(folder: str):
    return {
        subfolder: sum(
            len(fs) for dp, ds, fs in os.walk(os.path.join(folder, subfolder))
        )
        for subfolder in sorted(next(os.walk(folder))[1])
    }


count1 = get_file_count(folder1)
count2 = get_file_count(folder2)

for subfolder in sorted({*count1.keys(), *count2.keys()}):
    print(
        f"{subfolder[:40]:40} {count1.get(subfolder, 'NaN'):>6} {count2.get(subfolder, 'NaN'):>6}"
    )
