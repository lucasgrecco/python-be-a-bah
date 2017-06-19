print("Hello F. World\nteste ESTÃO \"Teste aspas duplas\" ")#aspas duplas escapa caracter
print("\n\n")
print('Hello F. World teste \n\'aspas simples NÃO\'')#aspas simples escapam.

string1 = "Olá\nMundo\nLegal 'Teste aspas'"
print(string1)

idade = 30
nome = 'Grecco'

print('Meu nome é %s e minha idaed é %d' %(nome, idade))#print de variáveis muito semelhante a C++

print('Teste de ' + 'concatenação')
print('Teste de '+str(idade))#str converte a variavel para String (toString)

print('Print no caracter especifico da String ' + nome[3])

#Brincando com Lists (Arrays)
print("Lists: ")
ar_teste = [0,1,2,3,4,5,6]#Lists sao arrays
print(ar_teste[2])
ar_referencia = ar_teste#isso cria um ponteiro
print(ar_referencia[2])
ar_copia = ar_teste.copy()#isso copia a lista
ar_copia[2] = 'teste'
print(ar_copia)
print('O Valor teste está na list ar_copia? ')
print('teste' in ar_copia)

#tuples sao lists nao modificaveis
print("Tuples: ")
tl_teste = ('um', 'dois', 'tres', 'quatro')
print(tl_teste)
print(tl_teste[2])

#dict - Dicionarios - Arrays
print("Dicionarios: ")
dict_teste = {"nome":"lucas", "idade":30, "nacionalidade":"brasileiro"}
print(dict_teste)

#for
for key,value in dict_teste.items():
    print('Chave - %s / Value - %s' %(key, str(value)))
    # print('Chave - ' + key + ' / Value - ' + str(value))
# import subprocess
# subprocess.call('clear', shell=True)

print("\nfor 2")
for nome in dict_teste:
    print(nome)

#while
i=0
while True:
    i = i+1
    print(i)
    if i == 10:
        break
print('\n\n')
i=0
for i in range(10):
    if i % 5 == 0:
        continue
    print(i)

def teste(valor):
    return valor

def dobra_valor(valor):
    return valor * 2

print(str(teste(99)))
print(dobra_valor(99))

from UtilsGrecco import Utils

dict_kwargs = {"nome":"lucas", "idade":30, "nacionalidade":"brasileiro"}
Utils.kwargs_teste(nome="lucas", idade=30, nacionalidade="brasileiro")