# main.py
from cli import criar_usuario, mostrar_usuarios, deletar_usuario, buscar_usuario_na_lista, atualizar_email_usuario
from database import usuarios, proximo_id

def menu():
    print("\n" + "=" * 40)
    print("       SISTEMA DE GERENCIAMENTO DE USUÁRIOS")
    print("=" * 40)
    print("1 - Criar usuário")
    print("2 - Mostrar usuários")
    print("3 - Buscar usuário")
    print("4 - Atualizar e-mail")
    print("5 - Remover usuário")
    print("6 - Sair")
    print("=" * 40)

while True:
    menu()
    try:
        opcao = int(input("Escolha uma opção (1-6): "))

        if opcao == 6:
            print("\nEncerrando o sistema. Até logo.")
            break
        elif opcao == 1:
            proximo_id = criar_usuario(usuarios, proximo_id)
        elif opcao == 2:
            mostrar_usuarios(usuarios)
        elif opcao == 3:
            buscar_usuario_na_lista(usuarios)
        elif opcao == 4:
            atualizar_email_usuario(usuarios)
        elif opcao == 5:
            deletar_usuario(usuarios)
        else:
            print("Opção inválida. Escolha entre 1 e 6.")
    except ValueError:
        print("Entrada inválida. Digite um número entre 1 e 6.")