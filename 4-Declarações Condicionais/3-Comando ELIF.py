# O computador sempre lê seus comandos de cima para baixo! (ELIF é uma abreviação de Else If)
def compare(x):
    if x>10:
        return 'Maior'
    elif x<0:
        return 'Negativo'
    elif x<10: 
        return 'Menor'
    else:
        return 'igual' 

print(compare(1))          