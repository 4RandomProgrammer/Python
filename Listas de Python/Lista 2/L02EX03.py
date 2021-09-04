#L02EX03

#Func
def desiverter(numero):
    numero = (numero % 10) * 10 + numero // 10
    return numero

#var
DiaEntrega = 0
MesEntrega = 0
DiaValidade = 0
MesValidade = 0
DiaAtual = 0
MesAtual = 0
i = 0

DiaEntrega = int(input())
MesEntrega = int(input())
DiaValidade = int(input())
MesValidade = int(input())

DiaEntrega = desiverter(DiaEntrega)
MesEntrega = desiverter(MesEntrega)
DiaValidade = desiverter(DiaValidade)
MesValidade = desiverter(MesValidade)

MesAtual = MesEntrega
DiaAtual = DiaEntrega + 3

if MesAtual > MesValidade or DiaAtual > DiaValidade:
    print(False)
else:
    print(True)