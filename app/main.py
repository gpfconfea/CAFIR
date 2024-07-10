import sys
sys.path.append('app')
from modules.files_manager import deleteFrom
from modules.menu import *
from modules.check_update import checkUpdate
from dados.baixar_dados import baixar_dados
from dados.sql import sqlserver
from dados.tabela_sql import tabela_sql
import os 


def runApp():
    option = mainMenu()

    #Baixar e montar tabela
    if option == 1:
        ans = confirmMenu(
            '''Esta opção irá apagar a base de dados atual e baixar sua atualização, 
este processo pode levar um tempo, Deseja continuar?'''
        )
        if ans == True:
            pastas = [
                os.path.join(os.path.dirname(__file__),
                             'dados', 'dados-publicos')]
            for p in pastas:
                deleteFrom(p, ignore_types=['.txt'])
            baixar_dados()
            sqlserver()

    #Baixar dados da Receita Federal
    elif option == 2:
        baixar_dados()

    #Montar banco de dados SQLite
    elif option == 3:
        if ans == True:
            pastas = [
                os.path.join(os.path.dirname(__file__),
                             'dados', 'dados-publicos')]
            for p in pastas:
                deleteFrom(p, ignore_types=['.txt'])
            sqlserver()
    
    elif option == 4:
        tabela_sql()

if __name__ == "__main__":
    checkUpdate()
    while True:
        runApp()