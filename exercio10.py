SJ = float(input("João entre com seu sálario:"))
CA1 = float(input("Entre com o valor da conta 1 que esta com pendência:"))
CA2 = float(input("Entre com o valor da conta 2 que esta com pendência:"))
M = CA1 + (2/100)* CA1 
M1 = CA2 + (2/100)* CA2 
SLF = SJ - (M + M1)
print("O valor da conta 1 com multas:",M)
print("O valor da conta 2 com multas:",M1)
print("O valor que irá sobrar do seu salário será R$:",SLF)

