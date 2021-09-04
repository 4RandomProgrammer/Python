#Ant CO-PIAH
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

#Func le textos
def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos
#'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

#'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

#'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

#'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
   # '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    result = 0
    counter = 0
    tamanho = len(as_b)
    while counter < tamanho:
        result += abs(as_a[counter] - as_b[counter])
        counter = counter + 1
    
    result = result/6


    return result

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #Valores que preciso calcular: wal,ttr,hlr,sal, sac e pal
    wal = 0 #Ok
    ttr = 0 #Ok
    hlr = 0 #Ok
    sal = 0 #EmFalta
    sac = 0 #
    pal = 0 #
    i = 0

    Numfrase = 0
    Numsetenca = 0
    Numpalavra = 0
    TamFrase = 0
    TamSetenca = 0
    TamPalavra = 0
    frase = []
    palavras = []
    templist = []
    tamanho_temp = 0

    #Todas a sentenças de um txt
    sentenca = separa_sentencas(texto)
    Numsetenca = len(sentenca)

    #Tentando pegar todas as frases do texto
    for countfrase in sentenca:

        templist = separa_frases(countfrase)
        TamSetenca += len(countfrase)
        tamanho_temp = len(templist)

        while i < tamanho_temp:
            frase.append(templist[i])
            i += 1

        i = 0

    Numfrase = len(frase)
    i = 0

    #Todas as plavras de um texto
    for countpalavra in frase:
        templist = separa_palavras(countpalavra)
        #O count palavra terá a frase então, só preciso pegar o tamanho dela
        TamFrase += len(countpalavra)
        tamanho_temp = len(templist)

        while i < tamanho_temp:
            palavras.append(templist[i])
            TamPalavra += len(templist[i])
            i += 1

        i = 0

    Numpalavra = len(palavras)


    wal = TamPalavra / Numpalavra
    ttr = n_palavras_diferentes(palavras) / Numpalavra
    hlr = n_palavras_unicas(palavras) / Numpalavra
    sal = TamSetenca / Numsetenca
    sac = Numfrase / Numsetenca
    pal = TamFrase / Numfrase
            
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    #'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 1
    tamanho = len(ass_cp)
    textoinfec = 0
    menor = ass_cp[0]
    while i < tamanho:
        if menor > ass_cp[i]:
            menor = ass_cp[i]
            textoinfec = i
        i += 1
    
    print("O autor do text", textoinfec ,"está infectado com COH-PIAH")
    return textoinfec

#Pegando assinatura do infectado e ja lendo os textos
assinaturas = []
grausimilaridade = []
assinaturainfec = le_assinatura()
textos = le_textos()

for texto in textos:
    assinaturas.append(calcula_assinatura(texto))

Len_assinaturas = len(assinaturas)
countass = 0
comp = 0
while countass < Len_assinaturas:
    comp = compara_assinatura(assinaturas[countass],assinaturainfec)
    grausimilaridade.append(comp)
    countass += 1


a = avalia_textos(textos,grausimilaridade)