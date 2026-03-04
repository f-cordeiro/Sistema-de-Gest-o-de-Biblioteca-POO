from item_biblioteca import ItemBiblioteca
from livro import Livro
from revista import Revista

class Biblioteca:
    def __init__(self):
        self.__itens = []
        self.__codigos_usados = set()

    def adicionar_item(self, item):
        if item.codigo in self.__codigos_usados:
            print(f"❌ Erro: Código '{item.codigo}' já existe!")
            return False
        self.__itens.append(item)
        self.__codigos_usados.add(item.codigo)
        print(f"✅ Item '{item.titulo}' cadastrado com sucesso!")
        return True

    def remover_item(self, codigo):
        for i, item in enumerate(self.__itens):
            if item.codigo == codigo:
                self.__itens.pop(i)
                self.__codigos_usados.remove(codigo)
                print(f"✅ Item '{item.titulo}' removido.")
                return True
        return False

    def listar_itens(self):
        print("\n--- Lista de Itens ---")
        if not self.__itens:
            print("Nenhum item cadastrado.")
        else:
            for item in self.__itens:
                print(f"{item.exibir_detalhes()} | {item.status_item()}")
        print("----------------------\n")

    def buscar_por_codigo(self, codigo):
        for item in self.__itens:
            if item.codigo == codigo:
                return item
        return None

    def verificar_disponibilidade(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            if item.disponivel:
                return f"✅ {item.titulo} - DISPONÍVEL"
            else:
                return f"❌ {item.titulo} - EMPRESTADO"
        else:
            return "❌ Item não encontrado."

    def relatorio_status(self):
        print("\n=== Relatório de Status ===")
        if not self.__itens:
            print("📭 Nenhum item cadastrado.")
        else:
            for item in self.__itens:
                print(f"{item.codigo} - {item.titulo} - {item.status_item()}")
        print("==========================\n")

    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            if item.emprestar():
                print(f"✅ Item '{item.titulo}' emprestado.")
            else:
                print("❌ Item já está emprestado.")
        else:
            print("❌ Item não encontrado.")

    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.devolver()
            print(f"✅ Item '{item.titulo}' devolvido.")
        else:
            print("❌ Item não encontrado.")