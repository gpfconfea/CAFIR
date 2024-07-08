import sys
sys.path.append('app/modules')
from menu import confirmMenu
import pandas as pd
import os


def deleteFrom(path, ignore_types=[], force=False):
    os.system("cls")
    print(f"Realizando limpeza em: {path}")

    try:
        files_to_remove = [os.path.join(path, file) for file in os.listdir(
            path) if os.path.splitext(file)[-1] not in ignore_types]
    except:
        print(f'Erro ao procurar arquivos. Tente novamente.')
        return False
    if len(files_to_remove) > 0:
        if force == False:
            if confirmMenu(f"Deseja visualizar os {len(files_to_remove)} arquivos a serem removidos?"):
                for file in files_to_remove:
                    print(file)
            if confirmMenu(f"Confirma excluir todos os {len(files_to_remove)} arquivos?"):
                for file in files_to_remove:
                    os.remove(file)
            else:
                print(f"Nenhum arquivo deletado de {path}.")
        else:
            for file in files_to_remove:
                os.remove(file)
            print("Arquivos deletados.")
    else:
        print("Nenhum arquivo para ser deletado.")


"""
Funções de padronização para
os arquivos CSV extraídos
"""


def dataCadastro(df):
    #formata a coluna 'data_inicio_atividades'
    def date(x): return f"{x[:4]}-{x[4:6]}-{x[6:8]}"
    df.Data_cadastro = df.Data_cadastro.astype(
        str).apply(date)
    # df.data_inicio_atividades = pd.to_datetime(
    #     df.data_inicio_atividades, errors='ignore')


def formatCep(df):
    #formata a coluna 'cep' no DataFrame
    def cep(x): return f"{x[:5]}-{x[5:]}"
    df.CEP = df.CEP.astype(str).str.zfill(8)
    df.CEP = df.CEP.apply(cep)


def formatDataFrame(df):
    #aplica todas as funções de formatação ao DataFrame
    formatCep(df)
    dataCadastro(df)
