class ClassTeste:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #print teste
    def print_teste(self):
        print(self.nome + ' ' + self.idade)

    #Printa o atributo caso ele exista
    def print_attr(self, attr):
        attr_string = str(attr)
        if hasattr(self, attr_string):
            print(getattr(self, attr_string))
        else:
            print("Atributo não definido.")