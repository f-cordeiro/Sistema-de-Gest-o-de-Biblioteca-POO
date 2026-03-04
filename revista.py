from item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, edicao, mes):
        super().__init__(codigo, titulo, ano)
        self.__edicao = edicao
        self.__mes = mes

    @property
    def edicao(self):
        return self.__edicao

    @edicao.setter
    def edicao(self, valor):
        self.__edicao = valor

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, valor):
        self.__mes = valor
