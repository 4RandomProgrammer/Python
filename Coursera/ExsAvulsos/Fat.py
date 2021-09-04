def main():
    while True:
        numero = int(input("Digite um numero: "))
        if numero < 0:
            break
        numero = fat(numero)
        print(numero)

def fat(numero):
    var = 1
    while numero != 1:
        var = numero * var
        numero -= 1

    return var

main()