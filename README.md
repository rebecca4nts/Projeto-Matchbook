MATCHBOOK - FUNCIONALIDADES

1 - menu inicial
- cadastro de usuário:
(recolhe nome, email, senha, cidade e estado onde o usuário mora. Verificações: o nome não pode conter números ou caracteres especiais além do hífen, o email deve ser de um domínio válido, ter @ e .com, a senha tem que ter até 7 dígitos, com letras, caracteres especiais e números, a cidade segue os mesmos parâmetros do nome, e o estado deve ser por UF, como PR, SP, PE, etc)

- login caso o usuário já seja cadastrado (pede email e senha, se estiverem ambos corretos, abre a aba de login, que explicarei mais a frente)

- sair (encerra o programa)

2- cadastro de livros
Após o usuário fazer seu cadastro, o programa recolhe os livros desejados (título, autor, gênero e edição) e livros ofertados (título, autor, gênero e edição), essa função fica em loop até que o usuário opte por ir para a etapa de busca por matches.
 
3- busca por matches
- compara os livros desejados e oferecidos do usuário com os dos usuários já cadastrados, para ser considerado o mesmo livro tem que ter o mesmo título, autor e gênero. Se o usuário estiver oferecendo pelo menos um livro desejado de qualquer um dos usuários cadastrados, desejar pelo menos um dos livros que um usuário cadastrado esteja oferecendo e se forem da mesma cidade e estado, serão considerados compatíveis pelo programa.

- mostra os usuários compatíveis, caso tenha algum, listando todos os livros que eles possuam ou desejam, sua localização e email para contato.

- caso não tenham usuários compatíveis, o programa exibe a mensagem “ops. não temos ninguém compatível no momento :(“ e um menu com 3 opções:
a. mostrar mais opções (pessoas que sejam minimamente compatíveis, seja por morar na mesma cidade ou pelos livros que oferecem e desejam)
b. cadastrar mais livros (volta a etapa de cadastro de livros) 
c. terminar por aqui (volta ao menu inicial).

4- aba de login
após o login bem-sucedido, o usuário tem as seguintes opções:
a. ver suas informações (nome, email, senha, cidade, estado e livros)
b. editar informações (pode editar seu nome, email, senha, cidade e estado)
c. editar livros (pode editar as informações dos livros desejados e oferecidos)
d. remover livros (pode deletar algum livro desejado ou oferecido)
e. adicionar livros (pode cadastrar mais livros desejados ou oferecidos)
f. voltar ao menu inicial

