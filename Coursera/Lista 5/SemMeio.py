#Exercicio 2

largura = int(input("Digite a largura: "))
altura = int(input("Digite a Altura: "))



#Counters
i = 0
j = 0

while i < altura:
    
    while j < largura:
        if i == 0 or i == altura - 1 or j == largura - 1 or j == 0:
            print("#",end='')
        else:
            print(" ",end='')

        j += 1
    print()
    j = 0
    i += 1
