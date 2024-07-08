def mainMenu():
    print(
        f"\n{' Bem-vindo! '.center(40, '*')}\n"
        f"\nEscolha uma das opções abaixo:\n"
    )

    option = int(input(
        "(1) Baixar e inserir dados na tabela CAFIR\n"
        "(2) Baixar dados CAFIR\n"
        "(3) Inserir dados na tabela"
        "(3) Criar tabela sql\n"
        "Sua resposta: "
    ))
    print("\n" + "".center(40, "*"))
    return option


def confirmMenu(texto_exibido='Confirma?'):
    """
    Exibe menu de confirmação que valida respostas de S/N

        Parameters:
            texto_exibido (str): Pergunta breve

        Returns:
            True or False
    """
    option = input(
        f"\n{texto_exibido} S/N\n"
        "\nSua resposta: "
    )
    return True if option.upper() == 'S' else False