#L02DESAFIO


#inputs
nBananas = int(input())


#var
nMafa = 1
bananasRes = 0
diaAnt = 0
diaCounter = 1
temp = 0

while diaAnt != nMafa:
    diaAnt = nMafa
    diaCounter += 1

    bananasRes = nBananas - nMafa

    if bananasRes < 0:
        nMafa -= bananasRes
    else:
        temp = bananasRes // 2
        if temp >= 2 * nMafa:
            nMafa = 2 * nMafa
        else:
            nMafa += temp

print(diaCounter)