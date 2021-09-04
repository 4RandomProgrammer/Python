#EX03L03

#Inputs
numinteracoes = int(input())

#var
kraiz = 0
k = 1
i = 0
j = 0

while i < numinteracoes:
    q = float(input())
    while j < 10:
        kraiz = (k + q/k)/2
        k = kraiz
        j += 1
    
    print(round(kraiz,2))

    i += 1
    j = 0
    kraiz = 0
    k = 1
    