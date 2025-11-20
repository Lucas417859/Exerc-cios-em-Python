
def somando (Entrada):
    soma = 0
    qtde = 0
    for i in Entrada:
        soma = soma + i
        qtde = len(Entrada)
    return(soma,qtde)
lista = [2, 4, 5]
Resultado = somando(lista)

print("A soma dos número são:",Resultado[0]) 
print("A quantidade de números que estão na lista é:",Resultado[1])   