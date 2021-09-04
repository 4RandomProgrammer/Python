#L02EX04

#inputs
CircJose = int(input())
PosJose = int(input())
CircFlav = int(input())
PosFlav = int(input())

#var
counterJose = 1
CounterFlav = 1
vivos = 0
PosVivo1 = 1
PosVivo2 = 1

while counterJose <= CircJose:
    PosVivo1 += 2
    if PosVivo1 > counterJose:
        PosVivo1 = 1
    counterJose += 1

if PosVivo1 == PosJose:
    vivos += 1


while CounterFlav <= CircFlav:
    PosVivo2 += 2
    if PosVivo2 > CounterFlav:
        PosVivo2 = 1
    CounterFlav += 1

if PosVivo2 == PosFlav:
    vivos += 1

print(vivos)