#maximo primo

def maior_primo(x):
    i = 2
    eprimo = True
    while True:

        while i < x / 2:
            if x % i == 0:
                eprimo = False
                break
            i += 1
        if eprimo:
            return x
            
        eprimo = True
        i = 2
        x -= 1
    