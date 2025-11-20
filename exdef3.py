
def contar_letra (texto,letra):
    contador = 0
    for caracter in texto:
        if caracter == letra:
            contador +=1
    return contador

T = input("Digite um texto:")
V = input("Qual vogal voce deseja consultar quantas vezes aparece no texto?:")
print("A quantide da letra",V,"aparece",contar_letra(T,V),"vezes no texto")         

        