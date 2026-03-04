from item_biblioteca import ItemBiblioteca
from livro import Livro
from revista import Revista

class Biblioteca:
    def __init__(self):
        self.__itens = []
        self.__codigos_usados = set()

