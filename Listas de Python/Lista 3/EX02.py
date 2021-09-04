#EX02L03

#var
dia0 = 0
dia1 = 1
temp = 0
i = 0

while True:
    mes = int(input())

    if mes == -1:
        break

    else:
        while i <= mes:
            print(dia1,end= " ")
            temp = dia1
            dia1 = dia0 + dia1
            dia0 = temp
            i += 1
    dia0  = 0
    temp = 0
    dia1 = 1
    i = 0
    print("¶")