

def cont_vogais(texto):       #Definindo a função, o nome da função, e o parametro.
    vogais = "aeiouAEIOU"     #Definindo as strings que são as vogais presente no alfabeto, para que na hora seja identificada no contador
    contador = 0              #Contador para contar quantas vogais tem no texto
    for Letra in texto:           #Para 'Letra' no texto
        if Letra in vogais:       #Se a Variável  'Letra' estiver na variavel vogais
            contador =  contador + 1      #Aqui o contador apenas será ativado se a função de cima for verdeira, então sera chamado o contador e ele vai adicionando a quantidade de vogais
    return contador                       #As maiorias das funções tem que ter um retorno, para retornar a função qunado acionada
Frase = input("Digite um texto:")
print("A quantidade de vogais no texto é:",cont_vogais(Frase))
