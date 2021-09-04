# L01EX05

HoraIni = int(input())

MinIni = int(input())

HoraFim = int(input())

MinFim = int(input())

HorasdeFesta = 0
MindeFesta = 0

# Precisa de if?

if HoraFim > HoraIni:
    HorasdeFesta = HoraFim - HoraIni

else:
    HorasdeFesta = HoraFim - HoraIni + 24

#Operação pros minutos
if MinFim >= MinIni:
    MindeFesta = MinFim - MinIni

else:
    MindeFesta = MinFim - MinIni  + 60
    HorasdeFesta -= 1

print("A festa durou " + str(HorasdeFesta) + " hora(s) e " + str(MindeFesta) + " minuto(s)")