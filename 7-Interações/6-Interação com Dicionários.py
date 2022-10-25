precos = {'macarrao':4, 'lasanha':5,'hamburguer':2}
quantidades = {'macarrao':6,'lasanha':10,'hamburguer':10}
gasto = 0
for x in precos:
    gasto += (precos[x]*quantidades[x])
    print(gasto)

