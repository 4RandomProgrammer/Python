#Numeros primordiais

#Inputs
entrada = int(input())

#Var
primos = 3
Calc = 2
i = 3
eprimo = True

while primos <= entrada:
    while i <= primos:
        if primos % i == 0 and i != primos:
            eprimo = False
            break
        i += 2
    if eprimo:
        Calc *= primos
    i = 3
    eprimo = True
    primos += 2

if entrada == 1:
    Calc = 1
    print(Calc)
elif entrada == 2:
    print(Calc)
elif entrada == 3:
    print(Calc*3)
elif entrada == 0:
    print("1")
else:
    print(Calc)