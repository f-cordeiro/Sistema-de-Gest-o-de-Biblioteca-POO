from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, autor, num_paginas):
        super().__init__(codigo, titulo, ano)
        self.__autor = autor
        self.__num_paginas = num_paginas

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        if valor and valor.strip():
            self.__autor = valor
        else:
            print("Erro: Autor não pode ser vazio.")

    @property
    def num_paginas(self):
        return self.__num_paginas

    @num_paginas.setter
    def num_paginas(self, valor):
        if valor and valor > 0:
            self.__num_paginas = valor
        else:
            print("Erro: Número de páginas deve ser maior que 0.")

    def exibir_detalhes(self):
        return f"📚 Livro: {self.titulo} | Autor: {self.__autor} | Páginas: {self.__num_paginas}"