def conta(numeros):
    total=0
    for x in numeros:
        if x<20:
            total +=1
    return total
lista = [1,3,7,8,19,54,86]
conta(lista)
