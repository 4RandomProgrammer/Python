#Jogo N|m

#Main, campeonato e partida


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    entrada = int(input("2 - para jogar um campeonato "))

    if entrada == 1:
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonato!")
        campeonato()


def campeonato():
    Pcvit = 0
    Usuariovit = 0
    rodada = 1
    while rodada <= 3:
        print("**** Rodada",rodada, "****")

        if partida() == 1:
            Usuariovit += 1
        else:
            Pcvit += 1

        rodada += 1

    print("**** Final do campeonato! ****")
    print("Placar: Você", Usuariovit, "X", Pcvit,"Computador")

def partida():
    playercomeca = False
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    a = 0

    if n % (m + 1) == 0:
        print("Voce começa!")
        a = usuario_escolhe_jogada(n, m)
        playercomeca = True
    else:
        print("Computador começa!")
        a = computador_escolhe_jogada(n, m)

    n -= a

    if playercomeca:
        
        while n > 0:
            n -= computador_escolhe_jogada(n,m)
            if n == 0:
                print("O computador venceu")
                playercomeca = False
                return 0
            n -= usuario_escolhe_jogada(n,m)
        if not playercomeca:
            print("O usuario venceu")
            return 1

    else:
        while n > 0:
            n -= usuario_escolhe_jogada(n,m)
            if n == 0:
                print("O usuario venceu")
                playercomeca = True
                return 1
            n -= computador_escolhe_jogada(n,m)
        if not playercomeca:    
            print("O computador venceu")
            return 0


def computador_escolhe_jogada(n, m):
    retirou = 1
    while (n - retirou) % (m + 1) != 0:
        if retirou > m:
            retirou = m
            break

        retirou += 1

    if retirou == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", retirou, "peças.")

    return retirou

def usuario_escolhe_jogada(n,m):
    x = int(input("Quantas peças você vai tirar? "))

    while(x > m):
            print("Oops! Jogada inválida! Tente de novo.")
            x = int(input("Quantas peças você vai tirar? "))

    if x == 1:
        print("Você tirou uma peça.")
    else:
        print("Voce tirou", x, "peças.")

    return x

main()