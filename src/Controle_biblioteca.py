import json
import os

# Constante para o nome do arquivo de dados
ARQUIVO_DADOS = "biblioteca.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Erro ao carregar base de dados. Iniciando vazia.")
            return []
    return []

def salvar_dados():
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(biblioteca, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar dados: {e}")

#Controle de biblioteca
biblioteca = carregar_dados()

def cadastrar_livro():
    livro = input("Digite o nome do livro: ").strip().title()
    
    if not livro:
        print("O nome do livro não pode ser vazio.")
        return

    for item in biblioteca:
        if item['nome'] == livro:
            print(f"O livro '{livro}' já está cadastrado.")
            return

    biblioteca.append({'nome': livro, 'quantidade': 0, 'total_exemplares': 0})
    salvar_dados()
    print(f"Livro {livro} cadastrado com sucesso!")

def listar_livros():
    if not biblioteca:
        print("Nenhum livro encontrado.")
    else:
        print("Livros encontrados:")
        for i, livro in enumerate(biblioteca):
            print(f"{i + 1}. {livro['nome']} - Disponíveis: {livro['quantidade']} / Total: {livro['total_exemplares']}")

def selecionar_livro():
    listar_livros()
    if not biblioteca:
        return None

    try:
        entrada = input("Digite o código do livro (ex: 1 para o primeiro) ou '0' para cancelar: ")
        codigo = int(entrada) - 1
        
        if codigo == -1:
            return None

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
                livro_selecionado['total_exemplares'] += quantia
                salvar_dados()
                print(f"{quantia} exemplares de '{livro_selecionado['nome']}' adicionados.")
            else:
                print("A quantidade deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def consultar_quantidade():
    livro_selecionado = selecionar_livro()
    if livro_selecionado:
        print(f"'{livro_selecionado['nome']}' tem {livro_selecionado['quantidade']} exemplares disponíveis.")

def realizar_emprestimo():
    livro_selecionado = selecionar_livro()
    if livro_selecionado:
        if livro_selecionado['quantidade'] >= 1:
            livro_selecionado['quantidade'] -= 1
            salvar_dados()
            print(f"Empréstimo de '{livro_selecionado['nome']}' realizado com sucesso.")
            print(f"Quantidade de exemplares restante: {livro_selecionado['quantidade']}")
        else:
            print(f"Livro '{livro_selecionado['nome']}' indisponível para empréstimo.")

def devolver_emprestimo():
    livro_devolucao = selecionar_livro()
    if livro_devolucao:
        if livro_devolucao['quantidade'] < livro_devolucao['total_exemplares']:
            livro_devolucao['quantidade'] += 1
            salvar_dados()
            print(f"Devolução de '{livro_devolucao['nome']}' realizada com sucesso.")
            print(f"Quantidade de exemplares restante: {livro_devolucao['quantidade']}")
        else:
            print("Não há exemplares emprestados deste livro. O livro não pertence à nossa biblioteca.")


def main():
    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Adicionar exemplares")
        print("4. Consultar quantidade")
        print("5. Realizar empréstimo")
        print("6. Devolver empréstimo")
        print("7. Sair")
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
            realizar_emprestimo()
        elif escolha == '6':
            devolver_emprestimo()
        elif escolha == '7':
            print("Sistema fechado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()