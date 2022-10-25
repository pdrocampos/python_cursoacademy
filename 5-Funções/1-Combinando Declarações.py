# Se Carlos poupou pelo menos 100 reais até o final de semana ele ganha + 15 reais de sua mãe 
# Mas
# Se ele não conseguir poupar pelo menos 1000R$ até o final de semana ele não ganha nada!

def adicione_15(m):
    if m>=100:
        m=m+15 
        return m 
    else:
        return('Guarda mais Carlos')

adicione_15(230)
adicione_15(99)
