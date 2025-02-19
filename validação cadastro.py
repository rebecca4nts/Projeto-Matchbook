import re
# Função para validar nome
def validar_nome(nome):
    if len(nome) < 3:
        print("Erro: O nome deve ter pelo menos 3 caracteres.")
        return False
    if not nome.replace(" ", "").isalpha():
        print("Erro: O nome não pode conter números ou caracteres especiais.")
        return False
    return True

# Função para validar e-mail
def validar_email(email):
    padrao_email = r"^[a-zA-Z0-9._%+-]+@(gmail|yahoo|outlook)\.com$"
    if not re.match(padrao_email, email):
        print("Erro: E-mail inválido. Certifique-se de usar um domínio válido (@gmail.com, @yahoo.com, @outlook.com).")
        return False
    return True

# Função para validar senha
def validar_senha(senha):
    if len(senha) > 7:
        print("Erro: A senha não pode ter mais de 7 caracteres.")
        return False
    if not any(char.isdigit() for char in senha):
        print("Erro: A senha deve conter pelo menos um número.")
        return False
    if not any(char in "!@#$%^&*()-_+=<>?/;:" for char in senha):
        print("Erro: A senha deve conter pelo menos um caractere especial (!@#$%^&*()-_+=<>?/;:).")
        return False
    return True

# Função para validar cidade
def validar_cidade(cidade):
    if len(cidade) < 2:
        print("Erro: O nome da cidade deve ter pelo menos 2 caracteres.")
        return False
    return True

# Função para validar estado
def validar_estado(estado):
    if len(estado) != 2 or not estado.isalpha():
        print("Erro: O estado deve conter exatamente 2 letras e não pode ter números ou caracteres especiais.")
        return False
    return True

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    while True:
        nome = input("\nDigite seu nome: ")
        if validar_nome(nome):
            break

    while True:
        email = input("Digite seu e-mail: ")
        if validar_email(email):
            break

    while True:
        senha = input("Crie uma senha: ")
        if validar_senha(senha):
            break

    while True:
        cidade = input("Digite sua cidade: ")
        if validar_cidade(cidade):
            break

    while True:
        estado = input("Digite seu estado (UF): ").upper()
        if validar_estado(estado):
            break