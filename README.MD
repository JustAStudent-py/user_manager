# 👤 Sistema de Gerenciamento de Usuários (CLI)

Uma aplicação simples e interativa de linha de comando (CLI) para gerenciar usuários.
Este projeto demonstra **arquitetura de código limpa**, separando responsabilidades em múltiplos módulos, tornando o código escalável e fácil de manter.

---

## ✨ Funcionalidades

* ➕ Criar novos usuários
* 📋 Listar todos os usuários
* 🔍 Buscar usuários por nome
* ✏️ Atualizar email do usuário
* ❌ Deletar usuários por ID
* ✅ Validação de entrada (nome e email)
* 🧠 Separação de responsabilidades (arquitetura modular)

---

## 🧱 Estrutura do Projeto

O projeto está organizado em múltiplos arquivos, seguindo uma estrutura usada no mercado:

```
user_system/
│
├── main.py        # Ponto de entrada da aplicação (loop principal)
├── cli.py         # Interface com o usuário (prints, menu, interações)
├── logic.py       # Regras de negócio
├── input.py       # Entrada de dados e validações simples
└── database.py    # Armazenamento em memória
```

---

## 🧠 Visão da Arquitetura

Cada arquivo possui uma **responsabilidade única**, facilitando manutenção e escalabilidade:

### 🔹 `input.py`

Responsável pela entrada de dados:

* Captura nome e email
* Normaliza os dados (lowercase e strip)
* Validação básica de email

---

### 🔹 `logic.py`

Contém as **regras de negócio**:

* Criação de usuário
* Validação de email
* Verificação de duplicidade
* Atualização e remoção

---

### 🔹 `cli.py`

Responsável pela **interação com o usuário**:

* Exibe menus
* Mostra mensagens
* Chama funções da lógica
* Interpreta respostas

---

### 🔹 `database.py`

Armazena o estado da aplicação:

* Lista de usuários
* ID incremental

---

### 🔹 `main.py`

Controla o fluxo do sistema:

* Executa o loop principal
* Lida com as opções do usuário
* Conecta todos os módulos

---

## 🚀 Como Executar

### 1. Clonar o repositório

```bash "
git clone https://github.com/seu-usuario/user-management-cli.git
cd user-management-cli
```

---

### 2. Rodar a aplicação

```bash "
python3 main.py
```

---

## 🖥️ Uso

Após rodar o programa, você verá:

```
========================================
        USER MANAGEMENT SYSTEM
========================================
1 - Criar usuário
2 - Mostrar usuários
3 - Buscar usuário
4 - Atualizar email
5 - Remover usuário
6 - Sair
========================================
```

Digite um número (1–6) para executar uma ação.

---

## 🧠 Como Funciona

### 🔹 Criação de Usuário

* Verifica se o nome não está vazio
* Valida o formato do email
* Evita emails duplicados

---

### 🔹 Atualização de Email

* Verifica se o usuário existe
* Valida o novo email
* Evita duplicidade

---

### 🔹 Remoção

* Remove o usuário pelo ID

---

## 📦 Modelo de Dados

Cada usuário é armazenado como um dicionário:

```
{
    "id": 1,
    "name": "john",
    "email": "john@email.com"
}
```

---

## ⚠️ Regras de Validação

* O email deve conter `@` e `.`
* Os nomes são normalizados (minúsculo e sem espaços extras)
* Emails devem ser únicos

---

## 🔧 Exemplo de Uso

```
> Create user
Enter user name: john
Enter user email: john@email.com
User created successfully.

> Show users
[1] Name: john | Email: john@email.com
```

---

## 🛠️ Melhorias Futuras

* 💾 Persistência de dados (SQLite, JSON ou banco de dados)
* 🔐 Sistema de autenticação
* 🌐 Criar uma API web (Flask ou FastAPI)
* 🧪 Testes automatizados


---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um fork 🍴
2. Crie uma branch 🌿
3. Envie um pull request 📬

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT.

---

## 💡 Por que este projeto?

Este projeto é ideal para:

* Iniciantes em Python 🐍
* Praticar arquitetura limpa
* Entender modularização
* Aprender operações CRUD

---

## ⭐ Apoio

Se este projeto te ajudou, considere dar uma estrela ⭐ no GitHub!

Bons estudos e bom código! 💻✨
