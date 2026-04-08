# cli.py
from helpers import obter_nome_e_email
from logic import criar_usuario_logica, atualizar_email_logica, deletar_usuario_logica, buscar_usuario

def criar_usuario(usuarios, proximo_id):
    print("\n=== CRIAR USUÁRIO ===")
    nome, email = obter_nome_e_email()
    resultado = criar_usuario_logica(nome, email, usuarios, proximo_id)

    if resultado == "nome_invalido":
        print("Nome inválido.")
        return proximo_id
    elif resultado == "email_invalido":
        print("E-mail inválido.")
        return proximo_id
    elif resultado == "email_existente":
        print("E-mail já cadastrado.")
        return proximo_id
    else:
        print("Usuário criado com sucesso.")
        return proximo_id + 1

def mostrar_usuarios(usuarios):
    print("\n=== LISTA DE USUÁRIOS ===")
    if usuarios:
        for usuario in usuarios:
            print(f"[{usuario['id']}] Nome: {usuario['name']} | E-mail: {usuario['email']}")
    else:
        print("Nenhum usuário cadastrado.")

def deletar_usuario(usuarios):
    print("\n=== REMOVER USUÁRIO ===")
    try:
        usuario_id = int(input("Digite o ID do usuário para remover: "))
    except ValueError:
        print("ID inválido.")
        return
    if deletar_usuario_logica(usuario_id, usuarios):
        print("Usuário removido com sucesso.")
    else:
        print("Usuário não encontrado.")

def buscar_usuario_na_lista(usuarios):
    print("\n=== BUSCAR USUÁRIO ===")
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return
    nome = input("Digite o nome para buscar: ").strip()
    usuario = buscar_usuario(nome, usuarios)
    if usuario:
        print(f"[{usuario['id']}] Nome: {usuario['name']} | E-mail: {usuario['email']}")
    else:
        print("Usuário não encontrado.")

def atualizar_email_usuario(usuarios):
    print("\n=== ATUALIZAR E-MAIL ===")
    nome, novo_email = obter_nome_e_email()
    resultado = atualizar_email_logica(usuarios, nome, novo_email)
    if resultado == "nao_encontrado":
        print("Usuário não encontrado.")
    elif resultado == "email_invalido":
        print("E-mail inválido.")
    elif resultado == "email_existente":
        print("E-mail já cadastrado.")
    else:
        print("E-mail atualizado com sucesso.")