#Numeros primos entre o intervalo

def n_primos(x):
    nprimos = 1
    i = 3
    divisor = 3
    eprimo = True
    if x == 3:
        nprimos += 1

        return nprimos
    else:
        while i < x:
            while divisor < i/2:
                if i % divisor == 0:
                    eprimo = False
                    break
                divisor += 2
            if eprimo:
                nprimos += 1

            eprimo = True
            divisor = 3
            i += 2

    return nprimos