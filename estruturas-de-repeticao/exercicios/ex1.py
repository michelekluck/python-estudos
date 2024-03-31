par = 0
impar = 0
for i in range(10):
    num = int(input("Digite o " + str(i+1) + " numero: "))
    if num % 2 == 0:
        par = par+1
    else:
        impar = impar+1
print(f"Você digitou {par} números pares e {impar} números impares")
     
        
