#EXERCICIO 4.1 SOFTWARE BASICO
SA = float(input("Entre com o seu salário atual:"))
PA = float(input("Entre com a porcentagem do seu aumento salaria:"))
NS = PA/100 * SA + SA
print("Seu novo salário com o reajuste de",PA,"é:R$",NS)