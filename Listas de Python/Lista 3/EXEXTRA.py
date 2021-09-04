#Rpg do Leeroy


#vidas
haeldraVida = 35
TakeshiVida = 10
odisVida = 8
fyravida = 8
atacouhaedra = 0

#Var
Comando = 2
fyrahab = True
haelperde = True

while haeldraVida > 0 and (TakeshiVida != 0 or odisVida != 0 or fyravida != 0):
    if haelperde:
        if haeldraVida < 8:
            haeldraVida += 4
            TakeshiVida -= 3
            odisVida -= 3
            fyravida -= 3
        elif atacouhaedra != 0:
            if atacouhaedra == 1:
                TakeshiVida -= 4
            elif atacouhaedra == 2:
                odisVida -= 4
            else:
                fyravida -= 4
        else:
            TakeshiVida -= 3
            odisVida -= 3
            fyravida -= 3

    if haelperde:
        haelperde = True 
    Comando = 3
    #Comando takeshi
    while TakeshiVida > 0:
        Comando = input()
        if Comando == "1":
            haeldraVida -= 5
            TakeshiVida -= 2
            atacouhaedra  = 1
            break
            
        elif Comando == "0":
            haeldraVida -= 4
            atacouhaedra  = 1
            break
    while odisVida > 0:
        Comando = input()
        
        if Comando == "0":
            haeldraVida -= 3
            atacouhaedra  = 2
            break
        elif Comando == "1":
            if TakeshiVida != 0:
                if TakeshiVida + 2 > 10:
                    TakeshiVida = 10
                else:
                    TakeshiVida += 2
            if odisVida != 0:
                if odisVida + 2 > 8:
                    odisVida = 8
                else:
                    odisVida += 2
            if fyravida != 0:
                if fyravida + 2 > 8:
                    fyravida = 8
                else:
                    fyravida += 2
            break
    while fyravida > 0:
        Comando = input()
        if Comando == "0":
            haeldraVida -= 4
            atacouhaedra  = 3
            break
        elif Comando == "1":
            if fyrahab:
                haelperde = False
                fyrahab = False
            break

if haeldraVida <= 0:
    print("Vitória!")
else:
    print("Derrota...")