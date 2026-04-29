maior = None

for i in range(5):
    num = float(input("Digite um número: "))

    if maior == None:
        maior = num

    if num > maior:
        maior = num
    

print(f"O maior número: {maior}")