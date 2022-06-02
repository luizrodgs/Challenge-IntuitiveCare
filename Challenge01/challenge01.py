import os
import requests
from shutil import make_archive


def download_file(url, file_address):
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(file_address, 'wb') as new_file:
            new_file.write(response.content)
        print('Download completed. File saved: {}'.format(file_address))
    else:
        response.raise_for_status()


def zip_files():
    make_archive('Files-Challenge01', 'zip', 'Output')
    print('Zip completed')


url_file1 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf'
url_file2 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.xlsx'
url_file3 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf'
url_file4 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf'
url_file5 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf'
url_list = [url_file1, url_file2, url_file3, url_file4, url_file5]


if __name__ == '__main__':
    output_dir = 'Output'
    c = 0
    for url in url_list:
        c += 1
        if url.endswith('.pdf'):
            file_name = os.path.join(output_dir, 'anexo{}.pdf'.format(c))
            download_file(url, file_name)
        elif url.endswith('.xlsx'):
            file_name = os.path.join(output_dir, 'anexo{}.xlsx'.format(c))
            download_file(url, file_name)
    zip_files()
