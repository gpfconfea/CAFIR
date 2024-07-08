import pyodbc
import pandas as pd
import os
from datetime import datetime
import time
from tqdm import tqdm

def sqlserver():
    campos_info = {
        'NIRF': 8,
        'Area_imovel': 9,
        'Cod_INCRA': 13,
        'Nome_imovel': 55,
        'Sit_imovel': 2,
        'Logradouro': 56,
        'Distrito_localizacao': 40,
        'UF': 2,
        'Municipio': 40,
        'CEP': 8,
        'Data_cadastro': 8,
        'Imune_isento': 3,
        'Cod_SNCR': 1}
    
    conn_str = (
    "Driver={SQL Server};"
    "Server=sgbdmain;"
    "Database=Fiscalizacao;"
    "Port=1433"
     ) 
    
    pasta_arquivos = r"app/dados/dados-publicos"
    # Conecta ao banco de dados SQL Server
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print('Carregando dados\n')
    # Itera sobre os arquivos na pasta
    log_file = 'app/dados/processed_files.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            processed_files = set(f.read().splitlines())
    else:
        processed_files = set() 

    for arq in os.listdir(pasta_arquivos):
        arquivo_txt = os.path.join(pasta_arquivos, arq)
        print('Início:', time.asctime())
        if arq in processed_files:
                print(f'O arquivo {arq} já foi processado. Pulando para o próximo arquivo.')
                print("\n*******************************************************************\n")
                continue
        
        print("\nInserindo dados de", arq)
        # Abre o arquivo de texto e insere os dados na tabela SQL Server
        with open(arquivo_txt, 'r', encoding='latin1') as file:
            for linha in tqdm(file):
                dados_linha = []
                cont = 0

                for campo_nome, campo_tam in campos_info.items():
                    campo = linha[cont:cont + campo_tam].strip()
                    if campo_nome == 'Data_cadastro':
                        try:
                            campo = datetime.strptime(campo, '%Y%m%d').strftime('%Y-%m-%d')
                        except ValueError:
                            campo = None
                    dados_linha.append(campo)
                    cont += campo_tam
                # Insere os dados na tabela SQL Server
                cursor.execute("INSERT INTO Fiscalizacao.cafir.dados_cafir VALUES (" + ", ".join(["?"] * len(campos_info)) + ")", tuple(dados_linha))

            with open(log_file, 'a') as f:
                f.write(f"{arq}\n")
                print(f'Arquivo {arq} processado e marcado como concluído.')
                print('Fim:', time.asctime())
    conn.commit()
    conn.close()
sqlserver()