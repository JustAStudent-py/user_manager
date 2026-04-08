# logic.py
from helpers import email_valido

def buscar_usuario(nome, usuarios):
    for usuario in usuarios:
        if usuario['name'] == nome:
            return usuario
    return None

def email_existente(email, usuarios):
    for usuario in usuarios:
        if usuario['email'] == email:
            return True
    return False

def criar_usuario_logica(nome, email, usuarios, proximo_id):
    if not nome:
        return "nome_invalido"
    if not email_valido(email):
        return "email_invalido"
    if email_existente(email, usuarios):
        return "email_existente"

    usuario = {"id": proximo_id, "name": nome, "email": email}
    usuarios.append(usuario)
    return usuario

def atualizar_email_logica(usuarios, nome, novo_email):
    usuario = buscar_usuario(nome, usuarios)
    if not usuario:
        return "nao_encontrado"
    if not email_valido(novo_email):
        return "email_invalido"
    if email_existente(novo_email, usuarios):
        return "email_existente"

    usuario['email'] = novo_email
    return "sucesso"

def deletar_usuario_logica(usuario_id, usuarios):
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuarios.remove(usuario)
            return True
    return False