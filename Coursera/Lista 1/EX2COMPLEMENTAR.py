numero = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = numero // (3600*24)
numero = numero % (3600*24)
horas = numero // 3600
numero = numero % 3600
minutos = numero // 60
numero = numero % 60

print(dias,"dias,",horas, "horas,",minutos, "minutos e",numero, "segundos.")