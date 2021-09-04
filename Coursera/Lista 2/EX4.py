#Se divisivel por 3  e por 5, imprimir fizz
num = int(input("Digite um numero: "))

if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")

else:
    print(num)