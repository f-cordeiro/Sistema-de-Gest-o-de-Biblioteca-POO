from biblioteca import Biblioteca
from livro import Livro
from revista import Revista

def menu():
    bib = Biblioteca()
    
    while True:
        print("\n" + "=" * 40)
        print("=== SISTEMA DE GESTÃO DE BIBLIOTECA ===")
        print("=" * 40)
        print("1. Cadastrar Livro")
        print("2. Cadastrar Revista")
        print("3. Listar Itens")
        print("4. Emprestar Item")
        print("5. Devolver Item")
        print("6. Consultar Disponibilidade")
        print("7. Relatório de Status")
        print("8. Sair")
        print("=" * 40)
        
        opcao = input("Escolha uma opção (1-8): ").strip()
        
        if opcao == '1':
            print("\n--- Cadastrar Livro ---")
            codigo = input("Código: ").strip()
            
            if not bib.buscar_por_codigo(codigo) is None:
                print("❌ Código já cadastrado! Escolha outro.")
                continue
            
            titulo = input("Título: ").strip()
            ano = int(input("Ano: "))
            autor = input("Autor: ").strip()
            paginas = int(input("Páginas: "))
            
            livro = Livro(codigo, titulo, ano, autor, paginas)
            bib.adicionar_item(livro)

        elif opcao == '2':
            print("\n--- Cadastrar Revista ---")
            codigo = input("Código: ").strip()
            
            if not bib.buscar_por_codigo(codigo) is None:
                print("❌ Código já cadastrado! Escolha outro.")
                continue
            
            titulo = input("Título: ").strip()
            ano = int(input("Ano: "))
            edicao = input("Edição: ").strip()
            mes = input("Mês: ").strip()
            
            revista = Revista(codigo, titulo, ano, edicao, mes)
            bib.adicionar_item(revista)

        elif opcao == '3':
            bib.listar_itens()

        elif opcao == '4':
            print("\n--- Emprestar Item ---")
            codigo = input("Código do item: ").strip()
            bib.emprestar_item(codigo)

        elif opcao == '5':
            print("\n--- Devolver Item ---")
            codigo = input("Código do item: ").strip()
            bib.devolver_item(codigo)

        elif opcao == '6':
            print("\n--- Consultar Disponibilidade ---")
            codigo = input("Código do item: ").strip()
            resultado = bib.verificar_disponibilidade(codigo)
            print(f"\n{resultado}\n")

        elif opcao == '7':
            bib.relatorio_status()

        elif opcao == '8':
            print("\n" + "=" * 40)
            print("Saindo do sistema...")
            print("Obrigado por usar o Sistema de Biblioteca!")
            print("=" * 40 + "\n")
            break

        else:
            print("\n Opção inválida! Escolha uma opção entre 1 e 8.\n")

if __name__ == "__main__":
    menu()