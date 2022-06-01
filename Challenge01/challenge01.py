import os
import requests


def download_file(url, file_address):
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(file_address, 'wb') as new_file:
            new_file.write(response.content)
        print('Download completed. File saved: {}'.format(file_address))
    else:
        response.raise_for_status()


if __name__ == '__main__':
    url_file1 = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf'
    output_dir = 'Downloads'

    file_name = os.path.join(output_dir, 'anexo.pdf')
    download_file(url_file1, file_name)
