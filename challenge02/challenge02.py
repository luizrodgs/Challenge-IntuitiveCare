import os
from shutil import make_archive

import pandas as pd
import pdfplumber


def exec02():
    with pdfplumber.open("Output/anexo1.pdf") as pdf:
        frames = []
        for page in pdf.pages:
            table = page.extract_table()
            if table is not None:
                frames.append(pd.DataFrame(table))
    pd.concat(frames).to_csv("Output2/anexo1.csv", index=False)
    zip_files()


def zip_files():
    """Zipa a pasta Output2 com os docs baixados"""
    if not os.path.isdir("Output2"):
        os.mkdir("Output2")
    make_archive("File-Challenge02", "zip", "Output2")
    print("Zip completed")


if __name__ == "__main__":
    exec02()
