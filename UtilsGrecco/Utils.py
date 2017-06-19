def teste(valor):
    return valor

def dobra_valor(valor):
    return valor * 2

def kwargs_teste(**kwargs):
    print("\nFunção Teste de KWArgs")
    for key, value in kwargs.items():
        print(key + ' - ' + str(value))