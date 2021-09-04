#Inverter a ordem

n = -1
Lista = []

while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break

    Lista.append(n)

lista_len = len(Lista) - 1
print()

while lista_len != -1:
    print(Lista[lista_len])
    lista_len -= 1