#EXERCICIO7.1 SOFTWARE BASICO
HT = int(input("Entre com as horas trabalhadas:"))
SM = int(input("Entre com o valor do salário mínimo:"))
H = SM/2
SB = HT*H
IM = 3/100 * SB 
SF = SB - IM
print("O valor de sua hora trabalhada é:",H)
print("O seu salário bruto é:",SB)
print("O valor do imposto descontado do seu salário é:",IM)
print("Seu salário final é:",SF)
