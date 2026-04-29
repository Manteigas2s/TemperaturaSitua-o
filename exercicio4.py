qnt_temp = int(input("Digite a quantidade de temperaturas que você deseja: "))
valor_temp = 0
soma = 0
maior = None
menor = None
historico = ""

for i in range(qnt_temp):
    temp_dia = float(input("Digite as temperaturas que deseja: "))
    soma += temp_dia 
    media = soma / qnt_temp
    
    if maior == None:
        maior = temp_dia
    
    if temp_dia > maior:
        maior = temp_dia
    
    if menor == None:
        menor = temp_dia
    
    if temp_dia < menor:
        menor = temp_dia
    
    historico = f" {media:.2f} - {maior:.2f} - {menor:.2f}\n"

print("---------------- HISTORICO DE TEMPERATURAS ----------------")
print(" MÉDIA | MAIOR | MENOR ")
print(historico)