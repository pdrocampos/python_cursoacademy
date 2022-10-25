#Outra maneira de adicionar dados 
from ast import Or


dicionario={'k1':'prato', 'k2':'garfo', 'k3':'faca', 'k4':'colher'}
dicionario
dicionario['k1']
dicionario['k3']
dicionario['k5'] = 'copo'
dicionario
dicionario['k2'] = 'panela'
dicionario
dep_trabalhores = {'dep_1':'Carlos', 'dep_2':['Marcela','Thaina','Neto']}
dep_trabalhores
dep_trabalhores['dep_2']
time = {}
time['Goleiro']='Claudio'
time['Zagueiro']='Bebeto'
time['Atacente']='Neymar'
time['Ponta Esquerda']='Pato'
time['Ponta Direita']='Robinho'
print(time)
print(time['Zagueiro'])
print(time.get('Atacente'))
print (time.get('técnico'))


