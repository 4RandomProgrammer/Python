#Digito adjacente

num = int(input("Digite um número inteiro: "))

dgtatual = 0
dgtanterio  = 50
seguidos = False

while num != 0:
    dgtatual = num % 10
    if dgtanterio == dgtatual:
        seguidos = True
        break
    dgtanterio = dgtatual
    num = num // 10

if seguidos:
    print("sim")
else:
    print("nao")

