# helpers.py

def obter_nome_e_email():
    print("\n=== ENTRADA DO USUÁRIO ===")
    nome = input("Digite o nome do usuário: ").lower().strip()
    email = input("Digite o e-mail do usuário: ").lower().strip()
    return nome, email    

def email_valido(email):
    return "@" in email and "." in email