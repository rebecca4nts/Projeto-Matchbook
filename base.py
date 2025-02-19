#função para validação de cadastro
import re

#usuários ficticios para a base de dados do programa
usuarios = [
    {
        "nome": "João",
        "email": "joao@example.com",
        "senha": "senha123",
        "cidade": "São Paulo",
        "estado": "SP",
        "livros_oferecidos": ["O Senhor dos Anéis", "1984", "Dom Casmurro"],
        "livros_desejados": ["O Pequeno Príncipe", "A Revolução dos Bichos"]
    },
    {
        "nome": "Maria",
        "email": "maria@example.com",
        "senha": "livros2024",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "livros_oferecidos": ["O Hobbit", "O Morro dos Ventos Uivantes"],
        "livros_desejados": ["1984", "Orgulho e Preconceito"]
    },
    {
        "nome": "Carlos",
        "email": "carlos@example.com",
        "senha": "segredo789",
        "cidade": "Belo Horizonte",
        "estado": "MG",
        "livros_oferecidos": ["Crime e Castigo", "Moby Dick"],
        "livros_desejados": ["O Grande Gatsby", "Harry Potter e a Pedra Filosofal"]
    },
    {
        "nome": "Ana",
        "email": "ana@example.com",
        "senha": "123abc",
        "cidade": "Curitiba",
        "estado": "PR",
        "livros_oferecidos": ["O Morro dos Ventos Uivantes", "Fahrenheit 451"],
        "livros_desejados": ["O Hobbit", "O Nome do Vento"]
    },
    {
        "nome": "Fernando",
        "email": "fernando@example.com",
        "senha": "livrolover",
        "cidade": "Porto Alegre",
        "estado": "RS",
        "livros_oferecidos": ["Memórias Póstumas de Brás Cubas", "O Código Da Vinci"],
        "livros_desejados": ["A Revolução dos Bichos", "O Pequeno Príncipe"]
    },
    {
        "nome": "Juliana",
        "email": "juliana@example.com",
        "senha": "trocalivros",
        "cidade": "Brasília",
        "estado": "DF",
        "livros_oferecidos": ["O Grande Gatsby", "O Hobbit"],
        "livros_desejados": ["Harry Potter e a Pedra Filosofal", "Cem Anos de Solidão"]
    },
    {
        "nome": "Gustavo",
        "email": "gustavo@example.com",
        "senha": "senha456",
        "cidade": "Salvador",
        "estado": "BA",
        "livros_oferecidos": ["Capitães da Areia", "A Menina que Roubava Livros"],
        "livros_desejados": ["O Código Da Vinci", "Crime e Castigo"]
    },
    {
        "nome": "Beatriz",
        "email": "beatriz@example.com",
        "senha": "livro123",
        "cidade": "Fortaleza",
        "estado": "CE",
        "livros_oferecidos": ["1984", "Orgulho e Preconceito"],
        "livros_desejados": ["Fahrenheit 451", "Memórias Póstumas de Brás Cubas"]
    },
    {
        "nome": "Ricardo",
        "email": "ricardo@example.com",
        "senha": "bookfan",
        "cidade": "Recife",
        "estado": "PE",
        "livros_oferecidos": ["As Crônicas de Nárnia", "O Senhor dos Anéis"],
        "livros_desejados": ["O Nome do Vento", "O Pequeno Príncipe"]
    },
    {
        "nome": "Larissa",
        "email": "larissa@example.com",
        "senha": "minhalista",
        "cidade": "Florianópolis",
        "estado": "SC",
        "livros_oferecidos": ["Cem Anos de Solidão", "A Revolução dos Bichos"],
        "livros_desejados": ["O Código Da Vinci", "Capitães da Areia"]
    }
]

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


 #loop para que o usuário possa cadastrar mais de um livro de uma só vez  
    livros_oferecidos = []
    while True:
        livro = input("De qual livro gostaria de se desfazer?:")
        livros_oferecidos.append(livro)
        continuar = input("Gostaria de adicionar mais algum livro? (s/n)").lower()
        if continuar != 's':
            break

    livros_desejados = []
    while True:
        livro = input("Qual livro gostaria de obter?:")
        livros_desejados.append(livro)
        continuar = input("Gostaria de adicionar mais algum livro? (s/n)").lower()
        if continuar != 's':
            break   
    
#para que o programa acesse a variaveis definidas anteriormente
    novo_usuario = {
        "nome": nome,
        "email": email, 
        "senha": senha,
        "cidade": cidade,
        "estado": estado,
        "livros_oferecidos": livros_oferecidos,
        "livros_desejados": livros_desejados
}

#adiciona o novo usuario à lista de usuarios cadastrados 
    usuarios.append(novo_usuario)
    return novo_usuario

#procura matches para o usuário (pessoas compatíveis)
def encontrar_match(usuario):
    matches = [u for u in usuarios if u["cidade"] == usuario["cidade"] and (set(u["livros_oferecidos"]) & set(usuario["livros_desejados"]) or set(u["livros_desejados"]) & set(usuario["livros_oferecidos"]))]
    
    if matches:
        print("Deu match! Você é compatível com:")
        for match in matches:
            print(f"- {match['nome']} da cidade {match['cidade']}")
            print("Como deseja prosseguir?")
            print("1. Entrar em contato")
            print("2. Cadastrar outros livros")
            print("3. Terminar por aqui")
            opcao_match = input("Escolha uma opção:") #caso existam usuários compatíveis 
            while opcao_match != "1" or "2" or "3":
                print("Insira uma opção válida")
            else:
                if opcao_match == "1":
                    print(f'{match['email']}')
                elif opcao_match == "2":
                    cadastrar_usuario()
                elif opcao_match == "3":
                    print("Encerrando programa...")


    else: #caso não existam usuários compatíveis
        print("Ops, infelizmente não temos ninguém compatível no momento, o que deseja fazer?")
        print("1. Mostrar mais opções")
        print("2. Cadastrar outros livros")
        print("3. Tentar novamente mais tarde")
        opcao_sem_match = input("Escolha uma opção: ")
        if opcao_sem_match == "1":
            mostrar_mais_opcoes(usuario)
        elif opcao_sem_match == "2":
            cadastrar_usuario()


def mostrar_mais_opcoes(usuario):
    opcoes = [u for u in usuarios if u["cidade"] != usuario["cidade"] and (set(u["livros_oferecidos"]) & set(usuario["livros_desejados"]) or set(u["livros_desejados"]) & set(usuario["livros_oferecidos"]))]
    
    if opcoes:
        print("Aqui estão algumas opções compatíveis em outras cidades:")
        for opcao in opcoes:
            print(f"- {opcao['nome']} da cidade {opcao['cidade']} ° contato: {opcao['email']}")
    else:
        print("Nenhuma opção disponível no momento.")

# Fluxo principal do programa
usuario = cadastrar_usuario()
encontrar_match(usuario)



