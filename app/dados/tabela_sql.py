import pyodbc

def tabela_sql():
    # Configurar a conexão
    dados_conexao = (
    "Driver={SQL Server};"
    "Server=sgbdmain;"
    "Database=Fiscalizacao;"
    "Port=1433"
     )

    # Conectar ao banco de dados
    try:
        conn = pyodbc.connect(dados_conexao)
        cursor= conn.cursor()
        print("\nConexão bem-sucedida!\n")

    except Exception as e:
        print("\nErro ao conectar ao banco de dados:", e, "\n")
    
    
    colunas= [ 
        'nirf char(8)',
        'area_imovel nvarchar(9)',
        'cod_incra varchar(13)',
        'nome_imovel nvarchar(55)',
        'sit_imovel int',
        'logradouro varchar(56)',
        'distrito_loc varchar(40)',
        'uf char(2)',
        'municipio varchar(40)',
        'cep char(8)',
        'atualizacao_cad date ',
        'imune_isento varchar(3)',
        'cod_sncr int'
                        ]
    def sqlCriaTabela(nomeTabela, colunas):
        sql = f'CREATE TABLE FFiscalizacao.cafir.{nomeTabela} ('
        for k, coluna in enumerate(colunas):
            sql += f'\n{coluna}'                
            if k+1 < len(colunas):
                sql += ','
        sql += '\n);'
        conn.commit()

        return sql

    sql = sqlCriaTabela('dados_cafir', colunas)
    cursor.execute(sql)

tabela_sql()