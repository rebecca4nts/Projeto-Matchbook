import os
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

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_nome(nome):
    return len(nome) >= 3 and nome.isalpha()

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@(gmail|yahoo|outlook)\.com$'
    return re.match(padrao, email) is not None

def validar_senha(senha):
    return len(senha) <= 7 and any(c.isdigit() for c in senha) and any(c in '!@#$%^&*' for c in senha)

def validar_cidade(cidade):
    #Verifica se a cidade tem pelo menos 3 letras e não contém números ou caracteres especiais.
    if len(cidade) < 3 or not cidade.replace(" ", "").isalpha():
        print("✕ Cidade inválida! Digite um nome válido (mínimo 3 letras, sem números ou caracteres especiais).")
        return False
    return True

def validar_estado(estado):
    #Verifica se o estado (UF) contém exatamente 2 letras e está na lista de estados brasileiros
    estados_validos = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SP", "SE", "TO"
    }
    
    if estado.upper() not in estados_validos:
        print("✕ UF inválida! Digite a sigla correta do estado (ex: SP, RJ, MG).")
        return False
    return True


def cadastrar_usuario():
    """Realiza o cadastro de um novo usuário com todas as validações."""
    usuarios = []  # Lista de usuários cadastrados

    nome = input("Digite seu nome: ")
    while not validar_nome(nome):
        nome = input("Digite seu nome novamente: ")

    email = input("Digite seu e-mail: ")
    while not validar_email(email):
        email = input("Digite seu e-mail novamente: ")

    senha = input("Digite sua senha: ")
    while not validar_senha(senha):
        senha = input("Digite sua senha novamente: ")

    cidade = input("Digite sua cidade: ")
    while not validar_cidade(cidade):
        cidade = input("Digite sua cidade novamente: ")

    estado = input("Digite seu estado (UF): ").upper()
    while not validar_estado(estado):
        estado = input("Digite sua UF novamente: ").upper()

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cidade": cidade,
        "estado": estado,
        "livros_oferecidos": [],
        "livros_desejados": []
    }
    return usuario

def cadastrar_livros(usuario):
    """Permite ao usuário cadastrar livros para troca"""
    livros_oferecidos = usuario.get("livros_oferecidos", [])
    livros_desejados = usuario.get("livros_desejados", [])

    print("\n✶ Cadastro de Livros ✶")
    while True:
        livro = input("De qual livro gostaria de se desfazer?: ").strip()
        if livro:
            livros_oferecidos.append(livro)
        continuar = input("Gostaria de adicionar mais algum livro? (s/n): ").lower()
        if continuar != 's':
            break

    while True:
        livro = input("Qual livro gostaria de obter?: ").strip()
        if livro:
            livros_desejados.append(livro)
        continuar = input("Gostaria de adicionar mais algum livro? (s/n): ").lower()
        if continuar != 's':
            break

    usuario["livros_oferecidos"] = livros_oferecidos
    usuario["livros_desejados"] = livros_desejados
    return usuario

def buscar_match(usuario, usuarios_cadastrados):
    """Busca um usuário compatível para troca de livros"""
    limpar_tela()
    print("\n⌕ Buscando um usuário compatível...\n")
    matches = []

    for u in usuarios_cadastrados:
        if u["email"] != usuario["email"]:
            if any(livro in u["livros_oferecidos"] for livro in usuario["livros_desejados"]) and \
               any(livro in usuario["livros_oferecidos"] for livro in u["livros_desejados"]):
                matches.append(u)

    if matches:
        print("★ Deu match! Você é compatível com:")
        for match in matches:
            print(f"⟡ {match['nome']} - ➮ {match['cidade']}/{match['estado']}")
            print(f"↻   Oferece: {', '.join(match['livros_oferecidos'])}")
            print(f"»   Deseja: {', '.join(match['livros_desejados'])}")
            print("-" * 40)
    else:
        print("\n✕ Ops! Nenhum match encontrado no momento.")
        while True:
            print("\nO que deseja fazer agora?")
            print("1️❏ - Mostrar mais opções")
            print("2️❏ - Cadastrar outros livros")
            print("3️❏ - Voltar ao menu principal")

            opcao = input("\nDigite a opção desejada: ").strip()

            if opcao == "1":
                mostrar_mais_opcoes(usuario, usuarios_cadastrados)
            elif opcao == "2":
                usuario = cadastrar_livros(usuario)
                return buscar_match(usuario, usuarios_cadastrados)
            elif opcao == "3":
                print("\n↺ Retornando ao menu principal...\n")
                return
            else:
                print("\n⚠ Opção inválida, tente novamente.")

def mostrar_mais_opcoes(usuario, usuarios_cadastrados):
    """Mostra opções de usuários que possuem pelo menos parte dos livros desejados"""
    print("\n⌕ Exibindo mais opções...")

    # Verifica se há usuários cadastrados
    print("Usuários cadastrados:", len(usuarios_cadastrados))
    
    encontrou_opcoes = False  # Flag para verificar se há opções disponíveis

    for u in usuarios_cadastrados:
        if u["email"] != usuario["email"]:  # Garante que não compara o usuário consigo mesmo
            
            # Normaliza os livros para comparação (remove espaços extras e padroniza para minúsculas)
            livros_oferecidos_u = [livro.lower().strip() for livro in u["livros_oferecidos"]]
            livros_desejados_u = [livro.lower().strip() for livro in u["livros_desejados"]]
            livros_oferecidos_usuario = [livro.lower().strip() for livro in usuario["livros_oferecidos"]]
            livros_desejados_usuario = [livro.lower().strip() for livro in usuario["livros_desejados"]]

            # Verifica se há ao menos um livro oferecido por U que o usuário deseja ou vice-versa
            if (any(livro in livros_oferecidos_u for livro in livros_desejados_usuario) or
                any(livro in livros_oferecidos_usuario for livro in livros_desejados_u)):

                encontrou_opcoes = True  # Indica que há opções compatíveis
                
                print(f"\n⟡ {u['nome']} - ➮ {u['cidade']}/{u['estado']}")
                print(f"    Oferece: {', '.join(u['livros_oferecidos'])}")
                print(f"    Deseja: {', '.join(u['livros_desejados'])}")
                print(f"   ✉ Contato: {(u['email'])}")
                print("-" * 40)
    
    if not encontrou_opcoes:
        print("\n✕ Nenhuma opção encontrada com os critérios especificados.")

# Fluxo principal do programa
usuario = cadastrar_usuario()
usuario = cadastrar_livros(usuario)
buscar_match(usuario, usuarios)  
