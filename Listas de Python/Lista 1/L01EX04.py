# L01EX04

ValorBase = int(input())

ValorProgressao = int(input())

TaxaGlicose = int(input())

Doses = 0

if TaxaGlicose >= ValorBase:
    Doses = 1 + (TaxaGlicose - ValorBase)//ValorProgressao

print(Doses)