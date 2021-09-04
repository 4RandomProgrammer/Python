#Fatorial

n = int(input("Digite o valor de n: "))

fatorial = 1

if n != 0:
    while n != 1:
        fatorial *= n
        n -= 1
    print(fatorial)
else:
    print(fatorial)