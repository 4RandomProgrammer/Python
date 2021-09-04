#Receber as temperaturas e dizer qual a maior e qual a menor

def maior(lista):
    maior = lista[0]

    for i in lista:
        if maior < i:
            maior = i

    return maior

def menor(lista):
    menor = lista[0]

    for i in lista:
        if menor > i:
            menor = i

    return menor
    
#Func principal
Temperaturas = []
counter = 0
leitor_temp = 0

while counter != 30:
    leitor_temp = int(input("Digite a temperatura: "))
    Temperaturas.append(leitor_temp)
    counter += 1

print(maior(Temperaturas))
print(menor(Temperaturas))
