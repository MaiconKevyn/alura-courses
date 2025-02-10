import os

restaurantes = [{'nome': 'Praça', 'categoria': 'pastel', 'ativo': False},
                {'nome': 'Sushi', 'categoria': 'sushi', 'ativo': True},
                {'nome': 'Pizza', 'categoria': 'pizza', 'ativo': False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def exibir_subtitulo(titulo):
    os.system('cls')
    linha = '*' * (len(titulo) + 4)
    print(linha)
    print(f'{titulo}')
    print(linha)

def finalizar_app():
    exibir_subtitulo('Finalizando o app')


def opcao_invalida():
    print('opcao invalida, digite novamente')
    input('digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante(restaurantes):
    exibir_subtitulo('Cadastro de novos restaurantes: ')

    nome_restaurante = input('Digite o nome do restaurante:')
    categoria = input('Digite a categoria do restaurante:')

    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_restaurante)

def mostrar_restaurantes(restaurantes):
    exibir_subtitulo('Os restaurantes cadastrados são:\n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

def voltar_ao_menu_principal():
    input('Pressione qualquer tecla para voltar ao menu principal')
    main()

def alternar_estado_do_restaurante():
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
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()