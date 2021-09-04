#Remoção de reptidos na lista
def remove_repetidos(lista):
    lista.sort()
    x = 0
    lista_len = len(lista) - 1
    while x < lista_len:
        if lista[x] == lista[x + 1]:
            del(lista[x])
            lista_len -= 1
        else:
            x += 1

    return lista
