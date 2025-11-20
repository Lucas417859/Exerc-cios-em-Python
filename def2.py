def somando(entrada):   #Definindo o nome da função e os parametros
    soma = 0            #A soma é igual a zero pois quando ela for passar no laço for ela vai ser somada aos números da lista, então por isso começa com 0 para não inteferir no resultado
    qtde = 0            #A quantidade tambem recebe um número 0 para que na hora de ser contado os números da quantidade de quantos números tem listas 
    for i in entrada:   #Aqui é um laço for, um loop pre estabelecido para no caso de código fazer as contas das somas dos número e da quantidade de números que tem na lista
        soma = soma + i #Aqui a gente esta declarando uma variavel "soma" onde ele soma o valor 0 de inicio com o "i", o "i" ele percorre todos os numeros da lista, somando ou contando, ou seja ele é uma variavel temporaria, e assume em ordem cade valor da lista
        qtde = len(entrada) #Aqui a função "Len" ela vai ler quantos números tem na lista, ou seja, quantidade de números.
    return (soma, qtde)

Lista = [4, 6, 8, 9]

resultado = somando(Lista) #Aqui estamos aplicando a função "somando" para a lista fornecida, onde acontecera tudo aquilo que foi estabelecido na função acima

print("O valor da lista somada é:", resultado[0]) #Aqui o 0 está entre [] para chamar a primeira função da tupla estabelecida que seria a soma, estabelecido no return(soma,qtde)
print("A quantidade de números da lista é:", resultado[1]) #Aqui o 1 está entre [] para chamar a segunda função da tupla estabelecida que seria a qtde, estabelecido no return(soma,qtde)
