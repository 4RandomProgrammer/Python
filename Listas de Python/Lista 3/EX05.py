#Caixa de gatos

altura = int(input())
largura = int(input())
espessura = int(input())

#var
i = 0
j = 0
AltGato = 0
LargGato = 0    
espCounter = espessura // 2

AltGato = altura // 2

LargGato = largura // 2


print(LargGato)

while i < altura:
    while j < largura:
        if j >= LargGato - espCounter and j < LargGato + espCounter  and i == AltGato:
            print(" ", end='')
        else:
            print("*", end='')
        j += 1
    print()
    j = 0
    i += 1