salario = float(input("Qual o seu salário?: "))
abono = 0
if salario < 5000:
    abono = 5000 * 0.15
else:
    abono = 5000 * 0.1
print(f"O valor do seu abono de fim de ano: R$ {abono:.2f}")