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


teste = ClassTeste("Lucas", "30 anos")
teste.print_teste()

teste.nome = "Lucas Grecco"
print(teste.nome)
print(hasattr(teste, "nome"))
print(hasattr(teste, "idade"))
print(hasattr(teste, "endereco"))
#setando atributo nao definido explicitamente
setattr(teste, "endereco", "aclimacao, peixoto oliveira.")#mesmo nao existindo o atributo, vc pode definir. Atua como uma classe generica
teste.print_attr("endereco")
# print(hasattr(teste, "endereco"))
print(teste.endereco)
delattr(teste, "endereco")
teste.print_attr("endereco")



