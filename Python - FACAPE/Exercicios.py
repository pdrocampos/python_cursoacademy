from asyncore import write
from email.errors import CloseBoundaryNotFoundDefect
from sys import float_repr_style
from tkinter import DoubleVar
from tokenize import Double
from unicodedata import decimal


print("Pedro")
A = 3
B = 5 
print(A+B)

nota1=10
nota2=9
nota3=2
nota4=3
media = (nota1+nota2+nota3+nota4)/4
print(media)

nome = input("Digite seu nome")
print("Você digitou %s" % nome)
print("Olá %s!" % nome)

a=int(input("Nota1: "))
b=int(input("Nota2: "))
c=int(input("Nota3: "))
d=int(input("Nota4: "))
media=int(a+b+c+d)/4
print('Sua média é igual a:', int(media))

anos = int(input("Digite o número de anos que você trabalhou: "))
valor_por_ano = int(input("Valor por ano foi de: "))
bonus = (anos * valor_por_ano)
print('O seu bônus foi de: ', bonus,'R$')

km_percorridos = int(input("Quantos km foram percorridos?"))
dias_alugados = int(input("Por quantos dias foi alugado?"))
aluguel_do_carro = dias_alugados * 60
aluguel_km_rodados = km_percorridos * 0.15
custo = aluguel_do_carro + aluguel_km_rodados
print("O custo total foi de:", custo ,"R$")

distancia = float(input("Digite o número que deseja converter: "))
distanciaMilimetro = (distancia * 1000)
print(f"O valor de {distancia}m em milímetros é {round(distanciaMilimetro,3)}mm")


temp_c = float(input("Quantos graos celsius?"))
temp_f = (temp_c * 9)/5 + 32
print(f"Sua temperatura em fahrenheit é: {round(temp_f,2)}")


valor_1 = int(input("Valor 1: "))
valor_2 = int(input("Valor 2: "))
if valor_1 > valor_2:
    print(f"{valor_1} é maior que {valor_2} !")
else:
   if valor_2 > valor_1:
    print(f"{valor_2} é maior que {valor_1} !")
   else: 
    print("Os números são iguais!")


temp_uso = int(input("Qual o tempo de uso do seu carro?"))
if temp_uso <= 3:
    print("Carro novo!")
if temp_uso > 3:
    print("Carro velho!")



km = int(input("Qual a sua velocidade?"))
if km > 80: 
    multa = (km - 80) * 5 
    print(f"Você foi mutado! O valor a pagar é de {multa}R$")
else: 
    print("Lembre-se o limite da rodovia é 80km/h")



min = int(input("Qual número de minutos você consumiu?"))
if min < 200:
    custo = min*0.20
    print(f"O valor a pagar é de {custo}R$")
if min >= 200 and min <= 400: 
       custo = min*0.18
       print(f"O valor a pagar é de {custo}R$")
if min > 400:
    custo = min*0.15
    print(f"O valor a pagar é de {custo}R$")




n1 = int(input("Número 01"))
n2 = int(input("Número 02"))
n3 = int(input("Número 03"))
if n1 != n2 and n1 != n3 and n3 !=n2:
    if n1 > n2 and n1 > n3 and n2 > n3:
        print(f"{n1} é o maior e o {n3} é o menor!")
    if n1 > n2 and n1 > n3 and n2 < n3:
        print(f"{n1} é o maior e o {n2} é o menor!")
    if n2 > n1 and n2 > n3 and n1 > n3:
        print(f"{n2} é o maior e o {n3} é o menor!")
    if n2 > n1 and n2 > n3 and n1 < n3: 
        print(f"{n2} é o maior e o {n1} é o menor!")
    if n3 > n1 and n3 > n2 and n1 > n2:
        print(f"{n3} é o maior e o {n2} é o menor!")
    if n3 > n1 and n3 > n2 and n1 < n2:
        print(f"{n3} é o maior e o {n1} é o menor")
else: 
    print("Alguns dos valores são iguais!")





x = 1
while x<=3:
    print(x)
    x = x+1 

contador = 0 
while contador < 5: 
    print(contador)
    contador = contador + 1


contador = 1
while contador <= 100:
    print(contador)
    contador = contador + 1 



contador = 10 
while contador >= 0:
    print(contador)
    contador = contador - 1
print("Fogoooo!")




contador = 1
max = int(input("Digite o número de contagem máxima: "))
while contador <= max:
    print(contador)
    contador = contador + 1 




tabuada = int(input("Digite o número que deseja a tabuada: "))
contador = 0 
while contador <=10: 
    resultado = tabuada * contador
    print(f"{tabuada} x {contador} = {resultado}")
    contador = contador + 1



valor_inic = float(input("Depósito inicial de: "))
saldo = valor_inic
taxa_de_juros = float(input("Taxa de juros em %: "))
mes = 1 
while mes <=12:
    saldo = saldo * (taxa_de_juros/100) + saldo
    print(f"Seu saldo com juros do mês {mes} é igual a: {round(saldo,2)}")
    mes = mes + 1
    if mes == 13:
        print(f"Seu juros total foi de {round (saldo - valor_inic,2)}")
    



a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b





n = int(input("Qual número que deseja obter a tabudada?"))
operador = str(input("Qual o tipo da tabuada? Soma (+) \n Subtração (-) \n Multiplicação (*) \n Divisão (/) \n"))
contador = 1
if n != 0:
    if operador == "+" or operador == "-" or operador == "*" or operador == "/":
        if operador == "+":
            while contador <= 10:
                resultado = n + contador  
                print(f"{n} {operador} {contador} = {resultado}")
                contador = contador + 1

        elif operador == "-":
            while contador <= 10:
                resultado = n - contador
                print(f"{n} {operador} {contador} = {resultado}")
                contador = contador + 1

        elif operador == "*":
            while contador <= 10:
                resultado = n * contador 
                print(f"{n} {operador} {contador} = {resultado}")
                contador = contador + 1

        elif operador == "/":
              while contador <= 10:
                resultado = n / contador
                print(f"{n} {operador} {contador} = {resultado}")
                contador = contador + 1
    else: 
        print("Operador inválido!!")            
else: 
    print("Número Inválido!!")   




nota = int(input("DIgite sua nota: "))
while (nota < 0) or (nota > 10):
    nota = int(input("Digite outra nota: "))
print("Nota válida!")





usuario = str(input("Login: "))
senha = str(input("Senha: "))

if senha == usuario: 
    while (senha == usuario):
        print("Erro: Sua senha não pode ser igual ao o usuário.")
        senha = str(input("Digite uma nova senha!"))
    print("Informações válidas!")
    print(f"Seu usuário é: {usuario}")
    print(f"Sua senha é: {senha}")
else: 
    print("Cadastro Realizado!")






nome = str(input("Qual o seu nome?"))
idade = int(input("Qual sua idade?"))
sexo = str(input("Qual seu sexo? \n 'M' 'F'")).upper()
salario = float(input("Qual o seu salário?"))
estado_civil = str(input("Qual seu Estado Civil? \n 'S' 'C' 'D' 'V' ")).upper()

while len(nome) < 3:
    print("Seu nome precisa ter mais de 3 caracteres!")
    nome = str(input("Digite seu nome: "))

while (idade < 0) or (idade > 150):
    print("Sua idade precisa estar entre 0 e 150 anos")
    idade = int(input("Digite sua idade: "))

while salario < 0: 
    print("Seu salário precisar ser maior que zero!")
    salario = float(input("Digite seu salário: "))

while (sexo != "F") and (sexo != "M"):
    print("Seu sexo está errado!")
    sexo = str(input("Digite seu sexo 'F' ou 'M': "))

while (estado_civil != "S") and (estado_civil != "C") and (estado_civil != "V") and (estado_civil != "D"):
    print("Seu Estado Civil está errado!")
    estado_civil = str(input("Seu Estado Civil é 'S' ou 'C' ou 'V' ou 'D': "))





numero = int(input("Digite um número!"))
while numero != 0:
    if numero%2 ==0:
        print("Número par!")
        numero = int(input("Digite outro número!"))
    else:
        print("Número ímpar!")
        numero = int(input("Digite outro número!"))
print("Valor inválido!")





continuar = "sim"
soma_par = 0
soma_impar = 0
contador = 1

while continuar == "sim":
    retornarOperacao = "sim"
    while retornarOperacao == "sim":
        soma_par = 0
        soma_impar = 0
        contador = 1

        while contador <= 6:
            numero = int(input("Digite um número"))
            if numero%2 == 0:
                print(f"{numero} é par")   
                soma_par+=numero 
            else:
                print(f"{numero} é ímpar")
                soma_impar+=numero
            contador+=1

        print(soma_par)
        print(soma_impar)
        retornarOperacao = input("Deseja retornar a operação?")

print("O programa se encerrou!")





print("===== Programa de Tabuada Iniciado ====")
retornarOperacao = "sim"
retornar = "sim"
while retornar == "sim":
    n = int(input("Informe um  número para obter a tabuada: "))
    retornarOperacao = "sim"
    while retornarOperacao == "sim":
        operacao = input(f"Digite o operador da tabuada de {n} \n(+) Tabuada de Soma \n(-) Tabuada de Subtração \n(*) Tabuada de Multiplicação \n(/) Tabuada de Divisão \n")
        propriedade = 0
        resultado = 0
       
        if n != 0  :
            if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":
                if  operacao == "+":
                    while propriedade < 10:
                        propriedade = propriedade + 1
                        resultado = n + propriedade
                        print(f"{n} {operacao} {propriedade} = {resultado}")
               
               
                elif operacao == "-":
                    while propriedade < 10:
                        propriedade = propriedade + 1
                        resultado = n - propriedade
                        print(f"{n} {operacao} {propriedade} = {resultado}")
               
                elif operacao == "*":
                    while propriedade < 10:
                        propriedade = propriedade + 1
                        resultado = n * propriedade
                        print(f"{n} {operacao} {propriedade} = {resultado}")
                       
                elif operacao == "/":
                    while propriedade < 10:
                        propriedade = propriedade + 1
                        resultado = n / propriedade
                        print(f"{n} {operacao} {propriedade} = {resultado:.2f}")
             
            else:
                 print("Operador Inválido!!")
        else:
            print("Número Inválido!!")
       
        retornarOperacao = input(f"Deseja usar {n} para realizar outra operaçao? ")
    retornar= input("Deseja obter uma tabuada com outro número?")

print("==== Programa Finalizado!====")

    



notas = [0,0,0,0,0]
soma = 0
x = 0

while x < 5:
    notas[x] = int(input(f"Digite sua Nota{x+1}: "))
    print("Nota %d: %6.2f" % (x+1, notas[x]))
    soma +=notas[x]
    x+=1 
print(f"Média: {round(soma,2)/x}")
x=0





listaDeInteiros = [0,0,0,0,0,0]
x = 0
posicao = 0
while x < 6:
    listaDeInteiros[x] = int(input(f"Digite o número da posição {x}: "))
    x+=1
print(listaDeInteiros)
while True:
    posicao = int(input("Digite a posição: \n Posição tem que ser maior ou igual a 0 e menor que 6. \n Para encerrar o programar é só digitar "))
    if posicao >= 0 and posicao < 6:
        x = posicao
        print(listaDeInteiros[x])
    else:
        print("O programa encerrou!")
        break
    




a = float(input())
b = float(input())
c = float(input())
delta = (b**2 - 4*a*c)

if a > 0 and delta >= 0:
    x1 = (- b + delta**(1/2)) / (2*a)
    x2 = (- b - delta**(1/2)) / (2*a)
    print(f"x1 = {x1/100} \nx2 = {x2/100}")
else: 
    print("Impossível calcular")




























