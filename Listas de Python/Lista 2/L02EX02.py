#L02EX02

#Var
Sinal = 0
Valor = 0

while Sinal != 'disconnect':
    Sinal = input()

    if Sinal != 'disconnect':
        Valor = Valor*10 + int(Sinal)

print(Valor)