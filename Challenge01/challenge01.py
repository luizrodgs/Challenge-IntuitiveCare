import os
import re
from shutil import make_archive

import requests
from bs4 import BeautifulSoup


def main():
    for c, url in enumerate(url_list):
        if url.endswith(".pdf"):
            file_name = os.path.join(output_dir, "anexo{}.pdf".format(c + 1))
            download_file(url, file_name)
        elif url.endswith(".xlsx"):
            file_name = os.path.join(output_dir, "anexo{}.xlsx".format(c + 1))
            download_file(url, file_name)
    zip_files()


def download_file(url, file_address):
    """Faz o download do doc referenciado"""
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(file_address, "wb") as new_file:
            new_file.write(response.content)
        print("Download completed. File saved: {}".format(file_address))
    else:
        response.raise_for_status()


def zip_files():
    """Zipa a pasta Output com os docs baixados"""
    make_archive("Files-Challenge01", "zip", "Output")
    print("Zip completed")


def collect_urls():
    base_response = requests.get(
        "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
    )
    base_content = base_response.content
    soup = BeautifulSoup(base_content, "html.parser")
    url_list = []
    for file_url in soup.find_all("a", string=re.compile("Anexo")):
        url_list.append(file_url["href"])
    return url_list


if __name__ == "__main__":
    output_dir = "Output"
    url_list = collect_urls()
    main()
