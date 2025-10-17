#EXERCICIO 4 SOFTWARE BASICO
V = float(input("Digite o valor de venda: "))
C = float(input("Digite o valor de compra : "))

lucro_percentual = ((V - C) / C) * 100

print(f"O lucro foi de {lucro_percentual:.2f}%")