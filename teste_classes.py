from ClassTesteAdvc import ClassTeste

teste = ClassTeste("Lucas", "30")
ClassTeste.print_teste(teste)
print(teste)


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