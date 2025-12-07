#Controle de biblioteca
biblioteca = []

def cadastrar_livro():
    livro = input("Digite o nome do livro: ").title()
    for item in biblioteca:
        if item['nome'] == livro:
            print(f"O livro '{livro}' já está cadastrado.")
            return

    biblioteca.append({'nome': livro, 'quantidade': 0})
    print(f"Livro {livro} cadastrado com sucesso!")

def listar_livros():
    if not biblioteca:
        print("Nenhum livro encontrado.")
    else:
        print("Livros encontrados:")
        for i, livro in enumerate(biblioteca):
            print(f"{i + 1}. {livro['nome']} - Quantidade: {livro['quantidade']}")

def selecionar_livro():
    listar_livros()
    if not biblioteca:
        return None

    try:
        codigo = int(input("Digite o código do livro (ex: 1 para o primeiro): ")) - 1
        if 0 <= codigo < len(biblioteca):
            return biblioteca[codigo]
        else:
            print("Código inválido.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return None

def adicionar_exemplares():
    livro_selecionado = selecionar_livro()
    if livro_selecionado:
        try:
            quantia = int(input("Digite a quantidade de exemplares a ser adicionada: "))
            if quantia > 0:
                livro_selecionado['quantidade'] += quantia
                print(f"{quantia} exemplares de '{livro_selecionado['nome']}' adicionados.")
            else:
                print("A quantidade deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def consultar_quantidade():
    livro_selecionado = selecionar_livro()
    if livro_selecionado:
        print(f"'{livro_selecionado['nome']}' tem {livro_selecionado['quantidade']} exemplares disponíveis.")

def realizar_empréstimo():
    livro_selecionado = selecionar_livro()
    if livro_selecionado:
        if livro_selecionado['quantidade'] >= 1:
            livro_selecionado['quantidade'] -= 1
            print(f"Empréstimo de '{livro_selecionado['nome']}' realizado com sucesso.")
            print(f"Quantidade de exemplares restante: {livro_selecionado['quantidade']}")
        else:
            print(f"Livro '{livro_selecionado['nome']}' indisponível para empréstimo.")

def main():
    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Adicionar exemplares")
        print("4. Consultar quantidade")
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

if __name__ == "__main__":
    main()