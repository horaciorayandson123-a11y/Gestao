import os
from estoque import Estoque, Produto


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_float(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("❌ O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido (ex: 15.99).")


def ler_int(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("❌ A quantidade não pode ser negativa. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida. Digite um número inteiro.")


def menu_principal():
    estoque = Estoque()

    while True:
        limpar_tela()
        print("=" * 40)
        print("       SISTEMA DE GESTÃO DE ESTOQUE      ")
        print("=" * 40)
        print("[1] Adicionar Novo Produto")
        print("[2] Atualizar Quantidade em Estoque")
        print("[3] Remover Produto")
        print("[4] Buscar Produto por Código")
        print("[5] Listar Todos os Produtos")
        print("[0] Sair")
        print("=" * 40)
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Adicionar Produto ---")
            codigo = input("Código único: ").strip()
            if not codigo:
                print("❌ O código não pode ser vazio.")
                input("\nPressione Enter para continuar..."); continue
                
            nome = input("Nome do produto: ").strip()
            quantidade = ler_int("Quantidade inicial: ")
            preco = ler_float("Preço unitário: R$ ")
            
            produto = Produto(codigo, nome, quantidade, preco)
            if estoque.adicionar_produto(produto):
                print("✅ Produto adicionado com sucesso!")
            else:
                print("❌ Erro: Já existe um produto com este código.")

        elif opcao == "2":
            print("\n--- Atualizar Estoque ---")
            codigo = input("Digite o código do produto: ").strip()
            produto = estoque.buscar_produto(codigo)
            if produto:
                print(f"Produto encontrado: {produto.nome} (Qtd Atual: {produto.quantidade})")
                nova_qtd = ler_int("Nova quantidade: ")
                estoque.atualizar_quantidade(codigo, nova_qtd)
                print("✅ Quantidade atualizada com sucesso!")
            else:
                print("❌ Produto não encontrado.")

        elif opcao == "3":
            print("\n--- Remover Produto ---")
            codigo = input("Digite o código do produto a ser removido: ").strip()
            if estoque.remover_produto(codigo):
                print("✅ Produto removido com sucesso!")
            else:
                print("❌ Produto não encontrado.")

        elif opcao == "4":
            print("\n--- Buscar Produto ---")
            codigo = input("Digite o código do produto: ").strip()
            produto = estoque.buscar_produto(codigo)
            if produto:
                print("\n📌 Detalhes do Produto:")
                print(produto)
            else:
                print("❌ Produto não encontrado.")

        elif opcao == "5":
            print("\n--- Lista de Produtos ---")
            produtos = estoque.listar_produtos()
            if produtos:
                for prod in produtos:
                    print(prod)
            else:
                print("O estoque está vazio.")

        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida! Escolha um número de 0 a 5.")
        
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    menu_principal()