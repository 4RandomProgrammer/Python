#L01EX06

topo = int(input())

carta = int(input())

if (topo % 13) == (carta % 13) or carta % 13 == 11:
    print("True")

elif (-12 <= (topo - carta)) and ((topo - carta) <= 12):
    print("True")

else:
    print("False")
