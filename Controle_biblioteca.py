#Controle de biblioteca
livros = []
quantidades = []
def cadastrar_livro():
    livro = input("Digite o nome do livro: ").title()
    livros.append(livro)
    print(f"Livro {livro} cadastrado com sucesso!")
    quantidade = int(0)
    quantidades.append(quantidade)

def listar_livros():
    if not livros:
        print("Nenhum livro encontrado.")
    else:
        print("Livros encontrados:")
        for i, livro in enumerate(livros):
            print(f"{i + 1}. {livro} - Quantidade: {quantidades[i]} ")

def adicionar_exemplares():
    codigo = int(input("Digite o codigo do livro (1 para primeiro, 2 para o segundo, etc.):"))-1
    quantia = int(input("Digite a quantidade de exemplares a ser adicionado: "))
    if 0 <= (codigo) < len(livros):
        quantidades[codigo] += quantia
        print(f"{quantia} exemplares de {livros[codigo]} adicionados.")
    else:
        print("Código inválido.")

def consultar_quantidade():
    codigo = int(input("Digite o código do livro (1 para primeiro, 2 para segundo, etc.): "))-1
    if 0 <= codigo < len(livros):
        print(f"{quantidades[codigo]} exemplares de {livros[codigo]} disponiveis")
    else:
        print("Código inválido.")

def realizar_empréstimo():
    codigo = int(input("Digite o código do livro (1 para primeiro, 2 para segundo, etc.): "))-1
    if 0 <= codigo < len(livros):
        if quantidades[codigo] >= 2:
            quantidades[codigo] -= 1
            print("Livro alugado")
            print(f"{livros[codigo]} alugado. Quantidade de exemplares restante: {quantidades[codigo]}")
        else:
            print("Livro indisponivel")
    else:
        print("Código inválido.")

while True:
    print("\nMenu:")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Adicionar exemplares")
    print("4. Consultar quantidade de exemplares")
    print("5. Realizar empréstimo")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        cadastrar_livro()
    elif escolha == '2':
        listar_livros()
    elif escolha == '3':
        adicionar_exemplares()
    elif escolha == '4':
        consultar_quantidade()
    elif escolha == '5':
        realizar_empréstimo()
    elif escolha == '6':
        print("Sistema fechado.")
        break
    else:
        print("Opção inválida. Tente novamente.")