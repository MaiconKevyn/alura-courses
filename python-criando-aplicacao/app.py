import os

restaurantes = [{'nome': 'Praça', 'categoria': 'pastel', 'ativo': False},
                {'nome': 'Sushi', 'categoria': 'sushi', 'ativo': True},
                {'nome': 'Pizza', 'categoria': 'pizza', 'ativo': False}]

def exibir_nome_do_programa():
    """
    Exibe o banner do programa 'Sabor Express' em ASCII art.
    Esta função não recebe parâmetros e não retorna valores.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    """
    Exibe o menu principal do programa com as opções disponíveis para o usuário.
    As opções incluem: cadastrar restaurante, listar restaurantes,
    alternar estado do restaurante e sair.

    Esta função não recebe parâmetros e não retorna valores.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def exibir_subtitulo(titulo):
    """
    Exibe um subtítulo formatado com decoração de asteriscos.

    Args:
        titulo (str): O texto que será exibido como subtítulo

    O subtítulo é formatado com uma linha de asteriscos acima e abaixo do texto,
    e a tela é limpa antes da exibição.
    """
    os.system('cls')
    linha = '*' * (len(titulo) + 4)
    print(linha)
    print(f'{titulo}')
    print(linha)

def finalizar_app():
    """
    Exibe a mensagem de finalização do aplicativo.
    Esta função não recebe parâmetros e não retorna valores.
    """
    exibir_subtitulo('Finalizando o app')


def opcao_invalida():
    """
    Trata o caso de uma opção inválida inserida pelo usuário.
    Exibe mensagem de erro, aguarda input do usuário e retorna ao menu principal.
    Esta função não recebe parâmetros e não retorna valores.
    """
    print('opcao invalida, digite novamente')
    input('digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante(restaurantes):
    """
    Cadastra um novo restaurante no sistema.

    Args:
        restaurantes (list): Lista de dicionários contendo os dados dos restaurantes

    O restaurante é cadastrado com nome, categoria e estado inicial desativado.
    Os dados são armazenados em um dicionário e adicionados à lista de restaurantes.
    """
    exibir_subtitulo('Cadastro de novos restaurantes: ')

    nome_restaurante = input('Digite o nome do restaurante:')
    categoria = input('Digite a categoria do restaurante:')

    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_restaurante)

def mostrar_restaurantes(restaurantes):
    """
    Exibe todos os restaurantes cadastrados no sistema em formato tabular.

    Args:
        restaurantes (list): Lista de dicionários contendo os dados dos restaurantes

    Mostra nome, categoria e status (ativado/desativado) de cada restaurante
    em um formato alinhado para melhor visualização.
    """
    exibir_subtitulo('Os restaurantes cadastrados são:\n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

def voltar_ao_menu_principal():
    """
    Pausa a execução até que o usuário pressione uma tecla e retorna ao menu principal.
    Esta função não recebe parâmetros e não retorna valores.
    """
    input('Pressione qualquer tecla para voltar ao menu principal')
    main()

def alternar_estado_do_restaurante():
    """
    Permite ativar ou desativar um restaurante específico.

    O usuário deve fornecer o nome do restaurante.
    Se encontrado, o estado (ativo/inativo) do restaurante é alternado
    e uma mensagem de confirmação é exibida.
    Se não encontrado, exibe mensagem de erro.
    """
    exibir_subtitulo('Alternar estado do restaurante: ')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante['nome']} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante['nome']} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

def escolher_opcao():
    """
    Processa a escolha do usuário no menu principal.

    Trata as seguintes opções:
    1 - Cadastrar restaurante
    2 - Listar restaurantes
    3 - Alternar estado do restaurante
    4 - Finalizar aplicação

    Inclui tratamento de exceções para entradas inválidas.
    """

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante(restaurantes)
            voltar_ao_menu_principal()

        elif opcao_escolhida == 2:
            print('Listar restaurantes')
            mostrar_restaurantes(restaurantes)
            voltar_ao_menu_principal()

        elif opcao_escolhida == 3:
            print('Alterar estado do restaurante')
            alternar_estado_do_restaurante()
            voltar_ao_menu_principal()

        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()
        main()

def main():
    """
    Função principal que inicia e controla o fluxo do programa.

    Realiza as seguintes operações:
    1. Limpa a tela
    2. Exibe o nome do programa
    3. Mostra as opções disponíveis
    4. Processa a escolha do usuário

    Esta função é o ponto de entrada principal do programa.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()