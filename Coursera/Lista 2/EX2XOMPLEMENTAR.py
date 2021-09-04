import math

#Ex de bhaskara, entradas serao os ter a,b e c

a = float(input("Entre a: "))
b = float(input("Entre b: "))
c = float(input("Entre c: "))

result = 0
result2 = 0

delta = b ** 2 - 4 * a * c
if delta == 0:
    result = - b / 2 * a
    print("a raiz desta equação é", result)

elif delta < 0:
    print("esta equação não possui raízes reais")

else:
    result = (- b + math.sqrt(delta)) / (2 * a)

    result2 = (- b - math.sqrt(delta)) / (2 * a)

    if result > result2:
        print("as raízes da equação são",result,"e", result2)
    else:
        print("as raízes da equação são",result2,"e", result)