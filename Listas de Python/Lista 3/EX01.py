#EX1L03

#inputs
qntdpartidas = int(input())

#var
i = 0
balas = 0
balasround = 1
recordAnt = 0
record = 0

while i < qntdpartidas:
    recordAnt = record
    record = int(input())

    if record > recordAnt:
        balas += balasround
        balasround += 1


    i += 1


print(balas)