#É ou n primo

num = int(input("Digite um número inteiro: "))
eprim = True
n = 2

while n < num / 2:
    if num % n == 0:
        eprim = False
        break
    n += 1

if eprim:
    print("primo")
else:
    print("não primo")