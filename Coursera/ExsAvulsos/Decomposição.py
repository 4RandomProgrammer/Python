#Decomposição em primos e multiplicidade dos termos


n = int(input("Digite um número inteiro, maior que 1: "))
multiplicidade = 0
fator = 3
eprimo = True

#Verificando apenas os 2 para que possa tirar seus multiplos da conta
if n % 2 == 0:
    while n % 2 == 0:
        multiplicidade += 1
        n = n // 2
    #Printa q é divisivel por 2 e a multiplicidade por 2
    print("É divisivel por 2 e sua multiplicidade é",multiplicidade)
    multiplicidade = 0

#Verificando os primos a partir de 3
while n != 1:
    i = 2
    #Conta para verificar se o fator for primo
    while i < fator // 2:
        if fator % i == 0:
            eprimo = False
    #Se o fator é primo e divide n, então faz a conta da multiplicidade
    if eprimo:
        while n % fator == 0:
            multiplicidade += 1
            n = n // fator

    if multiplicidade != 0:
        print("A mulplicidade de",fator,"é",multiplicidade)
        multiplicidade = 0
    
    fator += 2
    eprimo = True
