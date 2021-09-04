# L01EX03

x = int(input())

y = int(input())

Deise = 4*(x*x) + y*y

Silva = x*x*x + 2*(y*y)

Tabata = -50*x + y*y*y  

if Deise > Silva and Deise > Tabata:
    print("Deise venceu!")

elif Silva > Deise and Silva > Tabata:
    print("Silva venceu!")

elif Tabata > Deise and Tabata > Silva:
    print("Tabata venceu!")

else:
    print("Empate...    ")