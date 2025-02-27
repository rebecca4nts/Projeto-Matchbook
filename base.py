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
    },

    {"nome": "Ana", "email": "ana@gmail.com", "senha": "Ana@123", "cidade": "São Paulo", "estado": "SP", "livros_oferecidos": ["O Morro dos Ventos Uivantes"], "livros_desejados": ["O Hobbit"]},
    {"nome": "Julia", "email": "julia@yahoo.com", "senha": "Julia@456", "cidade": "Rio de Janeiro", "estado": "RJ", "livros_oferecidos": ["O Morro dos Ventos Uivantes"], "livros_desejados": ["1984"]},
    {"nome": "Carlos", "email": "carlos@gmail.com", "senha": "Car@789", "cidade": "Belo Horizonte", "estado": "MG", "livros_oferecidos": ["Dom Casmurro"], "livros_desejados": ["O Hobbit"]},
    {"nome": "Mariana", "email": "mariana@outlook.com", "senha": "Mari@321", "cidade": "Curitiba", "estado": "PR", "livros_oferecidos": ["A Revolução dos Bichos"], "livros_desejados": ["O Pequeno Príncipe"]},
    {"nome": "Rafael", "email": "rafael@gmail.com", "senha": "Rafa@654", "cidade": "Porto Alegre", "estado": "RS", "livros_oferecidos": ["O Senhor dos Anéis"], "livros_desejados": ["Dom Casmurro"]},
    {"nome": "Fernanda", "email": "fernanda@gmail.com", "senha": "Fern@123", "cidade": "Salvador", "estado": "BA", "livros_oferecidos": ["Memórias Póstumas de Brás Cubas"], "livros_desejados": ["1984"]},
    {"nome": "Lucas", "email": "lucas@yahoo.com", "senha": "Luc@456", "cidade": "Fortaleza", "estado": "CE", "livros_oferecidos": ["O Pequeno Príncipe"], "livros_desejados": ["A Revolução dos Bichos"]},
    {"nome": "Gabriela", "email": "gabriela@outlook.com", "senha": "Gabi@789", "cidade": "Manaus", "estado": "AM", "livros_oferecidos": ["Harry Potter e a Pedra Filosofal"], "livros_desejados": ["O Senhor dos Anéis"]},
    {"nome": "Fernando", "email": "fernando@gmail.com", "senha": "F3rn@123", "cidade": "Recife", "estado": "PE", "livros_oferecidos": ["1984"], "livros_desejados": ["Memórias Póstumas de Brás Cubas"]},
    {"nome": "Tatiane", "email": "tatiane@yahoo.com", "senha": "Tati@321", "cidade": "Brasília", "estado": "DF", "livros_oferecidos": ["O Hobbit"], "livros_desejados": ["Harry Potter e a Pedra Filosofal"]},
    {"nome": "André", "email": "andre@gmail.com", "senha": "Andr@654", "cidade": "Florianópolis", "estado": "SC", "livros_oferecidos": ["Dom Casmurro"], "livros_desejados": ["O Pequeno Príncipe"]},
    {"nome": "Vanessa", "email": "vanessa@outlook.com", "senha": "Vane@987", "cidade": "Goiânia", "estado": "GO", "livros_oferecidos": ["A Revolução dos Bichos"], "livros_desejados": ["O Morro dos Ventos Uivantes"]},
    {"nome": "Ricardo", "email": "ricardo@gmail.com", "senha": "Ric@234", "cidade": "Natal", "estado": "RN", "livros_oferecidos": ["1984"], "livros_desejados": ["Harry Potter e a Pedra Filosofal"]},
    {"nome": "Bianca", "email": "bianca@yahoo.com", "senha": "Bia@876", "cidade": "Belém", "estado": "PA", "livros_oferecidos": ["O Senhor dos Anéis"], "livros_desejados": ["Memórias Póstumas de Brás Cubas"]} 
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
def buscar_match(usuario):
    matches = [u for u in usuarios if u != usuario and (set(u["livros_oferecidos"]) & set(usuario["livros_desejados"]) and set(u["livros_desejados"]) & set(usuario["livros_oferecidos"]))]
    
    if matches:
        print("Deu match! Você é compatível com:")
        for match in matches:
            print(f"- {match['nome']} ({match['email']})")
    else:
        print("Ops, infelizmente não temos ninguém compatível no momento. O que deseja fazer?")
        while True:
            print("1. Mostrar mais opções")
            print("2. Cadastrar outros livros")
            print("3. Voltar ao início")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                opcoes = [u for u in usuarios if u != usuario and (set(u["livros_oferecidos"]) & set(usuario["livros_desejados"]) or set(u["livros_desejados"]) & set(usuario["livros_oferecidos"]))]
                if opcoes:
                    print("Aqui estão algumas opções para você:")
                    for op in opcoes:
                        print(f"- {op['nome']} ({op['email']})")
                else:
                    print("Nenhuma opção adicional encontrada.")
            elif opcao == "2":
                print("Voltando para cadastro de livros...")
                return "cadastro_livros"
            elif opcao == "3":
                print("Voltando ao menu principal...")
                return "menu_principal"
            else:
                print("Opção inválida. Tente novamente.")

# Fluxo principal do programa
usuario = cadastrar_usuario()
buscar_match(usuario)



