Atividade da Disciplina Tecnicas de programação do Curso de Licenciatura em Computação.
- 
Problema fictício
-
O IFPI Zona Sul deseja informatizar o controle de empréstimos de sua biblioteca. Para isso, o coordenador pediu aos alunos do curso de Computação que desenvolvessem um sistema simples para gerenciar o cadastro de livros e o empréstimo.

O sistema funcionará de forma semelhante a uma conta bancária, mas, em vez de saldo em dinheiro, haverá quantidade de livros disponíveis para cada título.

As funcionalidades do sistema serão:

- Cadastrar livro;

- Listar livros;

- Adicionar exemplares;

- Consultar quantidade disponível;

- Realizar empréstimo.

Funcionalidades do Sistema
-

**Cadastrar livro**
- O sistema solicita o nome do livro. Ao informar o título, ele é adicionado à lista de livros e, simultaneamente, é criada uma entrada na lista de quantidades, com valor inicial 0.

**Listar livros**
- O sistema exibe todos os títulos cadastrados e seus respectivos índices (códigos).

**Adicionar exemplares**
- O sistema solicita o código do livro e a quantidade de exemplares a adicionar. Essa quantidade é somada ao valor atual na lista de quantidades.

**Consultar quantidade disponível**
- O sistema solicita o código do livro e exibe a quantidade disponível no momento.

**Realizar empréstimo**
- O sistema solicita o código do livro e verifica se há pelo menos 1 exemplar disponível.

- Se houver, decrementa 1 da quantidade e exibe a mensagem "Empréstimo realizado".

- Caso contrário, exibe "Livro indisponível".