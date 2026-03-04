class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = True

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        if valor and valor.strip():
            self.__titulo = valor
        else:
            print("Erro: Título não pode ser vazio.")

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        if valor and valor > 0:
            self.__ano = valor
        else:
            print("Erro: Ano deve ser maior que 0.")

    @property
    def disponivel(self):
        return self.__disponivel
