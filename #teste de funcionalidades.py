#tudo ok

import re

# Lista para armazenar os usuários cadastrados
usuarios_cadastrados = [    {
        "nome": "joão",
        "email": "joao@yahoo.com",
        "senha": "senha123",
        "cidade": "são paulo",
        "estado": "sp",
        "livros_ofertados": [
            {"titulo": "o senhor dos anéis", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2019"},
            {"titulo": "1984", "autor": "george orwell", "genero": "distopia", "edicao": "2005"},
            {"titulo": "dom casmurro", "autor": "machado de assis", "genero": "romance", "edicao": "2006"}
        ],
        "livros_desejados": [
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "2015"},
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2010"}
        ]
    },
    {
        "nome": "maria",
        "email": "maria@gmail.com",
        "senha": "livros2024",
        "cidade": "rio de janeiro",
        "estado": "rj",
        "livros_ofertados": [
            {"titulo": "o hobbit", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2020"},
            {"titulo": "o morro dos ventos uivantes", "autor": "emily brontë", "genero": "romance", "edicao": "2012"}
        ],
        "livros_desejados": [
            {"titulo": "1984", "autor": "george orwell", "genero": "distopia", "edicao": "2021"},
            {"titulo": "orgulho e preconceito", "autor": "jane austen", "genero": "romance", "edicao": "2014"}
        ]
    },
    {
        "nome": "carlos",
        "email": "carlos@gmail.com",
        "senha": "segredo789",
        "cidade": "belo horizonte",
        "estado": "mg",
        "livros_ofertados": [
            {"titulo": "crime e castigo", "autor": "fiódor dostoiévski", "genero": "ficção", "edicao": "2000"},
            {"titulo": "moby dick", "autor": "herman melville", "genero": "aventura", "edicao": "1995"}
        ],
        "livros_desejados": [
            {"titulo": "o grande gatsby", "autor": "f. scott fitzgerald", "genero": "romance", "edicao": "2002"},
            {"titulo": "harry potter e a pedra filosofal", "autor": "j.k. rowling", "genero": "fantasia", "edicao": "2015"}
        ]
    },
    {
        "nome": "aurora",
        "email": "a_aurora@yahoo.com",
        "senha": "123abc",
        "cidade": "curitiba",
        "estado": "pr",
        "livros_ofertados": [
            {"titulo": "o morro dos ventos uivantes", "autor": "emily brontë", "genero": "romance", "edicao": "2009"},
            {"titulo": "fahrenheit 451", "autor": "ray bradbury", "genero": "distopia", "edicao": "2022"}
        ],
        "livros_desejados": [
            {"titulo": "o hobbit", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2022"},
            {"titulo": "o nome do vento", "autor": "patrick rothfuss", "genero": "fantasia", "edicao": "2001"}
        ]
    },
    {
        "nome": "fernando",
        "email": "fernando@yahoo.com",
        "senha": "livrolover",
        "cidade": "porto alegre",
        "estado": "rs",
        "livros_ofertados": [
            {"titulo": "memórias póstumas de brás cubas", "autor": "machado de assis", "genero": "romance", "edicao": "2001"},
            {"titulo": "o código da vinci", "autor": "dan brown", "genero": "suspense", "edicao": "1999"}
        ],
        "livros_desejados": [
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2004"},
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "2004"}
        ]
    },
    {
        "nome": "juliana",
        "email": "juliana@outlook.com",
        "senha": "trocalivros",
        "cidade": "brasília",
        "estado": "df",
        "livros_ofertados": [
            {"titulo": "o grande gatsby", "autor": "f. scott fitzgerald", "genero": "romance", "edicao": "2018"},
            {"titulo": "o hobbit", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2018"}
        ],
        "livros_desejados": [
            {"titulo": "harry potter e a pedra filosofal", "autor": "j.k. rowling", "genero": "fantasia", "edicao": "2018"},
            {"titulo": "cem anos de solidão", "autor": "gabriel garcía márquez", "genero": "realismo mágico", "edicao": "2010"}
        ]
    },
    {
        "nome": "gustavo",
        "email": "gustavo@gmail.com",
        "senha": "senha456",
        "cidade": "salvador",
        "estado": "ba",
        "livros_ofertados": [
            {"titulo": "capitães da areia", "autor": "jorge amado", "genero": "romance", "edicao": "2008"},
            {"titulo": "a menina que roubava livros", "autor": "markus zusak", "genero": "drama", "edicao": "2016"}
        ],
        "livros_desejados": [
            {"titulo": "o código da vinci", "autor": "dan brown", "genero": "suspense", "edicao": "2017"},
            {"titulo": "crime e castigo", "autor": "fiódor dostoiévski", "genero": "ficção", "edicao": "2015"}
        ]
    },
    {
        "nome": "beatriz",
        "email": "beatriz@gmail.com",
        "senha": "livro123",
        "cidade": "fortaleza",
        "estado": "ce",
        "livros_ofertados": [
            {"titulo": "1984", "autor": "george orwell", "genero": "distopia", "edicao": "2000"},
            {"titulo": "orgulho e preconceito", "autor": "jane austen", "genero": "romance", "edicao": "2009"}
        ],
        "livros_desejados": [
            {"titulo": "fahrenheit 451", "autor": "ray bradbury", "genero": "ficção científica", "edicao": "2022"},
            {"titulo": "memórias póstumas de brás cubas", "autor": "machado de assis", "genero": "romance", "edicao": "1998"}
        ]
    },
    {
        "nome": "ricardo",
        "email": "ricardo@yahoo.com",
        "senha": "bookfan",
        "cidade": "recife",
        "estado": "pe",
        "livros_ofertados": [
            {"titulo": "as crônicas de nárnia", "autor": "c.s. lewis", "genero": "fantasia", "edicao": "2022"},
            {"titulo": "o senhor dos anéis", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2021"}
        ],
        "livros_desejados": [
            {"titulo": "o nome do vento", "autor": "patrick rothfuss", "genero": "fantasia", "edicao": "2024"},
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "2002"}
        ]
    },
    {
        "nome": "larissa",
        "email": "larissa@outlook.com",
        "senha": "minhalista",
        "cidade": "florianópolis",
        "estado": "sc",
        "livros_ofertados": [
            {"titulo": "cem anos de solidão", "autor": "gabriel garcía márquez", "genero": "realismo mágico", "edicao": "2005"},
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2017"}
        ],
        "livros_desejados": [
            {"titulo": "o código da vinci", "autor": "dan brown", "genero": "suspense", "edicao": "2018"},
            {"titulo": "capitães da areia", "autor": "jorge amado", "genero": "ficção", "edicao": "2012"}
        ]
    },
    {
        "nome": "felipe",
        "email": "felps@gmail.com",
        "senha": "f3lp@123",
        "cidade": "recife",
        "estado": "pe",
        "livros_ofertados": [
            {"titulo": "1984", "autor": "george orwell", "genero": "distopia", "edicao": "2012"}
        ],
        "livros_desejados": [
            {"titulo": "memórias póstumas de brás cubas", "autor": "machado de assis", "genero": "romance", "edicao": "2014"}
        ]
    },
    {
        "nome": "tatiane",
        "email": "tatiane@yahoo.com",
        "senha": "tati@321",
        "cidade": "brasília",
        "estado": "df",
        "livros_ofertados": [
            {"titulo": "o hobbit", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2005"}
        ],
        "livros_desejados": [
            {"titulo": "harry potter e a pedra filosofal", "autor": "j.k. rowling", "genero": "fantasia", "edicao": "2011"}
        ]
    },
    {
        "nome": "andré",
        "email": "andre@gmail.com",
        "senha": "andr@654",
        "cidade": "florianópolis",
        "estado": "sc",
        "livros_ofertados": [
            {"titulo": "dom casmurro", "autor": "machado de assis", "genero": "romance", "edicao": "2011"}
        ],
        "livros_desejados": [
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "2015"}
        ]
    },
    {
        "nome": "joão",
        "email": "joao@example.com",
        "senha": "senha123",
        "cidade": "são paulo",
        "estado": "sp",
        "livros_ofertados": [
            {"titulo": "o senhor dos anéis", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2022"},
            {"titulo": "1984", "autor": "george orwell", "genero": "distopia", "edicao": "2009"},
            {"titulo": "dom casmurro", "autor": "machado de assis", "genero": "romance", "edicao": "2001"}
        ],
        "livros_desejados": [
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "1999"},
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2001"}
        ]
    },
    {
        "nome": "lucas",
        "email": "lucas@yahoo.com",
        "senha": "luc@456",
        "cidade": "fortaleza",
        "estado": "ce",
        "livros_ofertados": [
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "1981"}
        ],
        "livros_desejados": [
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2000"}
        ]
    },
    {
        "nome": "gabriela",
        "email": "gabriela@outlook.com",
        "senha": "gabi@789",
        "cidade": "manaus",
        "estado": "am",
        "livros_ofertados": [
            {"titulo": "harry potter e a pedra filosofal", "autor": "j.k. rowling", "genero": "fantasia", "edicao": "2005"}
        ],
        "livros_desejados": [
            {"titulo": "o senhor dos anéis", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2015"}
        ]
    },
    {
        "nome": "fernanda",
        "email": "fernanda@gmail.com",
        "senha": "fern@123",
        "cidade": "salvador",
        "estado": "ba",
        "livros_ofertados": [
            {"titulo": "memórias póstumas de brás cubas", "autor": "machado de assis", "genero": "romance", "edicao": "2016"}
        ],
        "livros_desejados": [
            {"titulo": "1984", "autor": "george orwell", "genero": "distopia", "edicao": "2001"}
        ]
    },
    {
        "nome": "mariana",
        "email": "mariana@outlook.com",
        "senha": "mari@321",
        "cidade": "curitiba",
        "estado": "pr",
        "livros_ofertados": [
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2003"}
        ],
        "livros_desejados": [
            {"titulo": "o pequeno príncipe", "autor": "antoine de saint-exupéry", "genero": "infantil", "edicao": "2003"}
        ]
    },
    {
        "nome": "rafael",
        "email": "rafael@gmail.com",
        "senha": "rafa@654",
        "cidade": "porto alegre",
        "estado": "rs",
        "livros_ofertados": [
            {"titulo": "o senhor dos anéis", "autor": "j.r.r. tolkien", "genero": "fantasia", "edicao": "2013"}
        ],
        "livros_desejados": [
            {"titulo": "dom casmurro", "autor": "machado de assis", "genero": "romance", "edicao": "2014"}
        ]
    },
    {
        "nome": "vanessa",
        "email": "vanessa@outlook.com",
        "senha": "vane@987",
        "cidade": "goiânia",
        "estado": "go",
        "livros_ofertados": [
            {"titulo": "a revolução dos bichos", "autor": "george orwell", "genero": "distopia", "edicao": "2007"}
        ],
        "livros_desejados": [
            {"titulo": "o morro dos ventos uivantes", "autor": "emily brontë", "genero": "romance", "edicao": "2007"}
        ]
    }]

# Função para validar o nome
def validar_nome(nome):
    return bool(re.match(r'^[A-Za-zÀ-ÿ\- ]+$', nome))

# Função para validar o email
dominios_validos = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com"] # Lista de domínios válidos

def validar_email(email):
    # Verifica se o email tem o formato básico correto
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return False
    
    # Extrai o domínio do email
    dominio = email.split('@')[-1].lower()
    
    # Verifica se o domínio está na lista de domínios válidos
    if dominio not in dominios_validos:
        return False
    
    return True

# Função para validar a senha
def validar_senha(senha):
    return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{1,7}$', senha))

# Função para validar a cidade
def validar_cidade(cidade):
    return bool(re.match(r'^[A-Za-zÀ-ÿ\- ]+$', cidade))

# Função para validar o estado (UF)
def validar_estado(estado):
    return estado.lower() in ["ac", "al", "ap", "am", "ba", "ce", "df", "es", "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr", "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc", "sp", "se", "to"]

# Função para cadastrar usuário
def cadastrar_usuario():
    print("-" * 30)
    print("Boas-Vindas ao MatchBook!")
    print("-" * 30)
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    while not validar_nome(nome):
        print("Nome inválido. Use apenas letras e hífen.")
        nome = input("Nome: ")
    
    email = input("Email: ")
    while not validar_email(email):
        print("Email inválido. Deve conter @ e .com.")
        email = input("Email: ")
    
    senha = input("Senha (até 7 dígitos, com letras, números e caracteres especiais): ")
    while not validar_senha(senha):
        print("Senha inválida. Deve ter até 7 dígitos, com letras, números e caracteres especiais.")
        senha = input("Senha: ")
    
    cidade = input("Cidade: ")
    while not validar_cidade(cidade):
        print("Cidade inválida. Use apenas letras e hífen.")
        cidade = input("Cidade: ")
    
    estado = input("Estado (UF): ")
    while not validar_estado(estado):
        print("Estado inválido. Use a sigla do estado (ex: SP, PR, RJ).")
        estado = input("Estado (UF): ")
    
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cidade": cidade,
        "estado": estado,
        "livros_desejados": [],
        "livros_ofertados": []
    }
    
    usuarios_cadastrados.append(usuario)
    print("\nUsuário cadastrado com sucesso!")
    return usuario

# Função para fazer login
def fazer_login():
    email = input("Email: ")
    senha = input("Senha: ")
    
    for usuario in usuarios_cadastrados:
        if usuario["email"] == email and usuario["senha"] == senha:
            print("Login bem-sucedido!")
            return usuario
    
    print("Email ou senha incorretos.")
    return None

# Função para cadastrar livros
def cadastrar_livros(usuario):
    while True:
        print("\n--- Cadastro de Livros ---")
        print("1. Adicionar livro desejado")
        print("2. Adicionar livro oferecido")
        print("3. Finalizar cadastro de livros")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("\nTítulo do livro desejado: ")
            autor = input("Autor do livro desejado: ")
            genero = input("Gênero do livro desejado: ")
            edicao = input("Edição do livro desejado: ")
            usuario["livros_desejados"].append({
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "edicao": edicao
            })
            print("\nLivro desejado adicionado!")
        
        elif opcao == "2":
            titulo = input("\nTítulo do livro oferecido: ")
            autor = input("Autor do livro oferecido: ")
            genero = input("Gênero do livro oferecido: ")
            edicao = input("Edição do livro oferecido: ")
            usuario["livros_ofertados"].append({
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "edicao": edicao
            })
            print("\nLivro oferecido adicionado!")
        
        elif opcao == "3":
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para buscar matches
def buscar_matches(usuario):
    matches_completos = []
    matches_parciais = []
    
    for outro_usuario in usuarios_cadastrados:
        if outro_usuario["email"] != usuario["email"]:
            # Verifica compatibilidade completa (mesma cidade, estado e livros em comum)
            livros_em_comum = False
            for livro_desejado in usuario["livros_desejados"]:
                for livro_ofertado in outro_usuario["livros_ofertados"]:
                    if (livro_desejado["titulo"] == livro_ofertado["titulo"] and
                        livro_desejado["autor"] == livro_ofertado["autor"] and
                        livro_desejado["genero"] == livro_ofertado["genero"] and
                        usuario["cidade"] == outro_usuario["cidade"] and
                        usuario["estado"] == outro_usuario["estado"]):
                        livros_em_comum = True
                        break
                if livros_em_comum:
                    break
            
            if livros_em_comum:
                matches_completos.append(outro_usuario)
            else:
                # Verifica compatibilidade parcial
                mesma_cidade_estado = (usuario["cidade"] == outro_usuario["cidade"] and
                                      usuario["estado"] == outro_usuario["estado"])
                
                tem_livros_em_comum = False
                for livro_desejado in usuario["livros_desejados"]:
                    for livro_ofertado in outro_usuario["livros_ofertados"]:
                        if (livro_desejado["titulo"] == livro_ofertado["titulo"] and
                            livro_desejado["autor"] == livro_ofertado["autor"] and
                            livro_desejado["genero"] == livro_ofertado["genero"]):
                            tem_livros_em_comum = True
                            break
                    if tem_livros_em_comum:
                        break
                
                if mesma_cidade_estado or tem_livros_em_comum:
                    matches_parciais.append(outro_usuario)
    
    # Mostra matches completos
    if matches_completos:
        print("Deu match! Você é compatível com:")
        print("\n------- / / / / / -------")
        for match in matches_completos:
            print(f"Nome: {match['nome']}")
            print(f"Email: {match['email']}")
            print(f"Cidade: {match['cidade']}, Estado: {match['estado']}")
            print("Livros Ofertados:")
            for livro in match["livros_ofertados"]:
                print(f"  - {livro['titulo']} por {livro['autor']} ({livro['genero']})")
            print("Livros Desejados:")
            for livro in match["livros_desejados"]:
                print(f"  - {livro['titulo']} por {livro['autor']} ({livro['genero']})")
            print("-----------------------------")
    else:
        print("Ops. Não temos ninguém compatível no momento :(")
        while True:
            print("\n1. Mostrar mais opções")
            print("2. Cadastrar mais livros")
            print("3. Terminar por aqui")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                if matches_parciais:
                    print("\n--- Usuários Parcialmente Compatíveis ---")
                    for match in matches_parciais:
                        print(f"Nome: {match['nome']}")
                        print(f"Email: {match['email']}")
                        print(f"Cidade: {match['cidade']}, Estado: {match['estado']}")
                        print("Livros Ofertados:")
                        for livro in match["livros_ofertados"]:
                            print(f"  - {livro['titulo']} por {livro['autor']} ({livro['genero']})")
                        print("Livros Desejados:")
                        for livro in match["livros_desejados"]:
                            print(f"  - {livro['titulo']} por {livro['autor']} ({livro['genero']})")
                        print("-----------------------------")
                else:
                    print("Não há usuários parcialmente compatíveis no momento.")
                break
            elif opcao == "2":
                cadastrar_livros(usuario)
                buscar_matches(usuario)
                break
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

# Função para exibir informações do usuário
def ver_informacoes(usuario):
    print("\n--- Suas Informações ---")
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"Senha: {usuario['senha']}")
    print(f"Cidade: {usuario['cidade']}, Estado: {usuario['estado']}")
    print("Livros Desejados:")
    for livro in usuario["livros_desejados"]:
        print(f"  - {livro['titulo']} por {livro['autor']} ({livro['genero']})")
    print("Livros Ofertados:")
    for livro in usuario["livros_ofertados"]:
        print(f"  - {livro['titulo']} por {livro['autor']} ({livro['genero']})")

# Função para editar informações do usuário
def editar_informacoes(usuario):
    print("\n--- Editar Informações ---")
    nome = input("Novo nome: ")
    while not validar_nome(nome):
        print("Nome inválido. Use apenas letras e hífen.")
        nome = input("Nome: ")
    usuario["nome"] = nome
    
    email = input("Novo email: ")
    while not validar_email(email):
        print("Email inválido. Deve conter @ e .com.")
        email = input("Email: ")
    usuario["email"] = email
    
    senha = input("Nova senha (até 7 dígitos, com letras, números e caracteres especiais): ")
    while not validar_senha(senha):
        print("Senha inválida. Deve ter até 7 dígitos, com letras, números e caracteres especiais.")
        senha = input("Senha: ")
    usuario["senha"] = senha
    
    cidade = input("Nova cidade: ")
    while not validar_cidade(cidade):
        print("Cidade inválida. Use apenas letras e hífen.")
        cidade = input("Cidade: ")
    usuario["cidade"] = cidade
    
    estado = input("Novo estado (UF): ")
    while not validar_estado(estado):
        print("Estado inválido. Use a sigla do estado (ex: SP, PR, RJ).")
        estado = input("Estado (UF): ")
    usuario["estado"] = estado
    
    print("Informações atualizadas com sucesso!")

# Função para editar livros
def editar_livros(usuario):
    while True:
        print("\n--- Editar Livros ---")
        print("1. Editar livros desejados")
        print("2. Editar livros oferecidos")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            for i, livro in enumerate(usuario["livros_desejados"]):
                print(f"{i+1}. {livro['titulo']} por {livro['autor']} ({livro['genero']})")
            indice = int(input("Escolha o número do livro para editar: ")) - 1
            if 0 <= indice < len(usuario["livros_desejados"]):
                titulo = input("Novo título: ")
                autor = input("Novo autor: ")
                genero = input("Novo gênero: ")
                edicao = input("Nova edição: ")
                usuario["livros_desejados"][indice] = {
                    "titulo": titulo,
                    "autor": autor,
                    "genero": genero,
                    "edicao": edicao
                }
                print("Livro desejado atualizado!")
            else:
                print("Índice inválido.")
        
        elif opcao == "2":
            for i, livro in enumerate(usuario["livros_ofertados"]):
                print(f"{i+1}. {livro['titulo']} por {livro['autor']} ({livro['genero']})")
            indice = int(input("Escolha o número do livro para editar: ")) - 1
            if 0 <= indice < len(usuario["livros_ofertados"]):
                titulo = input("Novo título: ")
                autor = input("Novo autor: ")
                genero = input("Novo gênero: ")
                edicao = input("Nova edição: ")
                usuario["livros_ofertados"][indice] = {
                    "titulo": titulo,
                    "autor": autor,
                    "genero": genero,
                    "edicao": edicao
                }
                print("Livro oferecido atualizado!")
            else:
                print("Índice inválido.")
        
        elif opcao == "3":
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para remover livros
def remover_livros(usuario):
    while True:
        print("\n--- Remover Livros ---")
        print("1. Remover livros desejados")
        print("2. Remover livros oferecidos")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            for i, livro in enumerate(usuario["livros_desejados"]):
                print(f"{i+1}. {livro['titulo']} por {livro['autor']} ({livro['genero']})")
            indice = int(input("Escolha o número do livro para remover: ")) - 1
            if 0 <= indice < len(usuario["livros_desejados"]):
                usuario["livros_desejados"].pop(indice)
                print("Livro desejado removido!")
            else:
                print("Índice inválido.")
        
        elif opcao == "2":
            for i, livro in enumerate(usuario["livros_ofertados"]):
                print(f"{i+1}. {livro['titulo']} por {livro['autor']} ({livro['genero']})")
            indice = int(input("Escolha o número do livro para remover: ")) - 1
            if 0 <= indice < len(usuario["livros_ofertados"]):
                usuario["livros_ofertados"].pop(indice)
                print("Livro oferecido removido!")
            else:
                print("Índice inválido.")
        
        elif opcao == "3":
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para adicionar livros
def adicionar_livros(usuario):
    while True:
        print("\n--- Adicionar Livros ---")
        print("1. Adicionar livro desejado")
        print("2. Adicionar livro oferecido")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título do livro desejado: ")
            autor = input("Autor do livro desejado: ")
            genero = input("Gênero do livro desejado: ")
            edicao = input("Edição do livro desejado: ")
            usuario["livros_desejados"].append({
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "edicao": edicao
            })
            print("Livro desejado adicionado!")
        
        elif opcao == "2":
            titulo = input("Título do livro oferecido: ")
            autor = input("Autor do livro oferecido: ")
            genero = input("Gênero do livro oferecido: ")
            edicao = input("Edição do livro oferecido: ")
            usuario["livros_ofertados"].append({
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "edicao": edicao
            })
            print("Livro oferecido adicionado!")
        
        elif opcao == "3":
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Função para a aba de login
def aba_login(usuario):
    while True:
        print("\n--- Menu de Login ---")
        print("1. Ver suas informações")
        print("2. Editar informações")
        print("3. Editar livros")
        print("4. Remover livros")
        print("5. Adicionar livros")
        print("6. Voltar ao menu inicial")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ver_informacoes(usuario)
        elif opcao == "2":
            editar_informacoes(usuario)
        elif opcao == "3":
            editar_livros(usuario)
        elif opcao == "4":
            remover_livros(usuario)
        elif opcao == "5":
            adicionar_livros(usuario)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função principal do programa
def main():
    while True:
        print("\n--- Menu Inicial ---")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuario = cadastrar_usuario()
            cadastrar_livros(usuario)
            buscar_matches(usuario)
        elif opcao == "2":
            usuario = fazer_login()
            if usuario:
                aba_login(usuario)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()