#L02EX05

#func
def nDigitos(digito):
    soma = 0
    loop = 0

    while digito > loop:
        count = loop

        while count != 0:

            soma = soma + count % 2
            count = count // 2


        
        if soma % 2 == 1:
            print("1",end='')
        else:
            print("0",end='')

        soma = 0
        loop += 1

    

#var
n = int(input())


nDigitos(n)
print('')