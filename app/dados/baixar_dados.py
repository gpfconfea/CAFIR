def baixar_dados():
    from bs4 import BeautifulSoup
    import requests
    import wget
    import os
    import sys
    import time
    import glob

    url = 'https://dadosabertos.rfb.gov.br/CAFIR/'

    # local dos arquivos zipados da Receita
    pasta_compactados = r"app/dados/dados-publicos"

    if len(glob.glob(os.path.join(pasta_compactados, '*.csv'))):
        print(
            f'Há arquivos na pasta {pasta_compactados}. Apague ou mova esses arquivos e tente novamente')
        sys.exit()

    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data)
    lista = []
    print('Relação de Arquivos em ' + url)
    for link in soup.find_all('a'):
        cam = link.get('href')
        if cam and not cam.startswith('http') and 'csv' in cam:
            # if cam.startswith('http://http'):
            #     cam = 'http://' + cam[len('http://http//'):]
            if not cam.startswith('http'):
                print(url+cam)
                lista.append(url+cam)
            else:
                print(cam)
                lista.append(cam)

    resp = input(
        f'Deseja baixar os arquivos acima para a pasta {pasta_compactados} (s/n)?')
    if resp.lower() != 'y' and resp.lower() != 's':
        sys.exit()

    def bar_progress(current, total, width=80):
        if total >= 2**20:
            tbytes = 'Megabytes'
            unidade = 2**20
        else:
            tbytes = 'kbytes'
            unidade = 2**10
        progress_message = f"Baixando: %d%% [%d / %d] {tbytes}" % (
            current / total * 100, current//unidade, total//unidade)
        # Don't use print() as it will print in new line every time.
        sys.stdout.write("\r" + progress_message)
        sys.stdout.flush()

    for k, url in enumerate(lista):
        print('\n' + time.asctime() + f' - item {k}: ' + url)
        wget.download(url, out=os.path.join(pasta_compactados,
                      os.path.split(url)[1]), bar=bar_progress)

    print('\n\n' + time.asctime() +
          f' Finalizou!!! Baixou {len(lista)} arquivos.')

    
#baixar_dados()