#fatorial

def fatorial(x):
    if x == 0:
        x = 1
    else:
        while x != 1:
            x *= x
            x -= 1

    return x

n = int(input())
k = int(input())

coefbinamial = fatorial(n)/(fatorial(k) * (fatorial(n - k)))

print(coefbinamial)