def contar_vogais(texto):
    contador = 0
    vogais ='AEIOUaeiou'
    for letra in texto:
        if letra in vogais:
            contador = contador + 1
    return contador
L = input("Entre com uma palavra ou texto:")
print("A quantidade de vogais no texto é:",contar_vogais(L))