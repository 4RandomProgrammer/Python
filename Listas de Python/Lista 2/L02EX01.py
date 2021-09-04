#L02EX01

#Variaveis
n = int(input())
i = 0
valpar = 0
valimpar = 0
valpositivo = 0
valnegativo = 0 

while i < n:
    x = int(input())

    if x % 2 == 1 or x % 2 == -1:
        valimpar += 1
    else:
        valpar += 1
    if x >= 0:
        valpositivo += 1
    else:
        valnegativo += 1
    i += 1

print(valpar," valor(es) par(es)")
print(valimpar," valor(es) impar(es)")
print(valpositivo," valor(es) positvo(s)")
print(valnegativo," valor(es) negativo(s)")