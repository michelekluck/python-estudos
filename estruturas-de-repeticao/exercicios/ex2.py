menor = 0
maior = 0
for i in range(5):
    num = int(input("Digite o " + str(i+1) + " número: "))
    if i == 0 or num < menor:
        menor = num
    if num > maior:
        maior = num
print(f"O menor número digitado foi {menor} e o maior foi {maior}")