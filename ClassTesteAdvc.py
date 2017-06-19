from ClassTeste import ClassTeste


class ClassTesteAdvc(ClassTeste):

    contador = 0

    def __init__(self, nome, idade, cep):
        ClassTeste.__init__(self, nome, idade)
        self.cep = cep
        ClassTesteAdvc.contador += 1#vira uma global

    def print_cep(self):
        print(self.cep)


teste_avancado = ClassTesteAdvc('lucas', '30', '01415001')
teste_avancado1 = ClassTesteAdvc('lucas', '30', '01415001')
teste_avancado2 = ClassTesteAdvc('lucas', '30', '01415001')
teste_avancado.print_cep()
print(teste_avancado.contador)
print(teste_avancado1.contador)
print(teste_avancado2.contador)





