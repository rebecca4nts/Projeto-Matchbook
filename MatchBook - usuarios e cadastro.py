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

#função para cadastro de novos usuarios
def cadastrar_usuario():
    nome = input("Insira seu nome:")
    email = input("Insira seu e-mail:")
    senha = input("Insira sua senha (use até 8 caracteres, contendo letras, números e caracteres especiais):")
    cidade = input("Insira sua cidade:")
    estado = input("Insira seu estado (UF):")

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




