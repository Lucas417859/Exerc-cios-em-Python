#EXERCICIO 5 SOFTWARE BASICO
N = int(input("Entre com o valor do estoque anterior:"))
P = int(input("Entre com o valor do estoque atual:"))
NE = ((P - N) / N) * 100
print("Valor do estuque anterior:",N)
print("Valor do estoque atual:",P)
print(f"O aumento em porcentagem do estoque foi:{NE:.2f}%")