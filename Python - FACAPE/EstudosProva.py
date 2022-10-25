

depositoInicial = float(input("Digite o depósito inicial: "))
subtracao = depositoInicial 
taxaDeJuros = float(input("Digite a taxa de juros: "))
mes = 1
while mes <= 12:
	depositoInicial = (depositoInicial*taxaDeJuros/100) + depositoInicial
	print(f"No mês {mes} o seu resultado é de: {round(depositoInicial,2)}")
	mes+=1
print(f"O total ganho com juros é de: {round(depositoInicial - subtracao,2)}")






nota = int(input("Digite sua nota: \n valido apenas notas entre 0 e 10"))
while nota < 0 or nota > 10:
	nota = int(input("Digite sua nota: \n valido apenas notas entre 0 e 10"))	
print("Nota Válida")





usuario = input("Digite sua senha: ")
senha = input("Digite sua senha: ")

while senha == usuario:
	print("A senha inválida, pois é igual ao o usuário.")
	senha = input("Digite sua senha: ")
print("Usuário Cadastrado")








nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo: ")
estadoCivil = input("Digite seu Estado Civil: ")

while len(nome) < 3:
	print("Nome tem que ser maior que 3 caracteres!")
	nome = input("Digite seu nome: ")
	print(nome)
while idade > 150 and idade < 0:
	print("Idade tem que ser entre 0 e 150!")
	idade = int(input("Digite sua idade: "))
	print(idade)
while salario < 0:
	print("Seu Salário tem que ser maior que zero!")
	salario = float(input("Digite seu salário: "))
	print(salario)
while sexo != "f" and sexo != "m":
	print("Seu sexo tem que ser igual a 'f' ou 'm'!")
	sexo = input("Digite seu sexo: ")
	print(sexo)
while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
	print("Seu Estado Civil tem que ser igual a 's','c','v' ou 'd'!")
	estadoCivil = input("Digite seu Estado Civil: ")
	print(estadoCivil)







numero = int(input("Digite um número:  \n Digite '0' para finalizar o programa!"))
while numero != 0:
	numero = int(input("Digite um número:  \n Digite '0' para finalizar o programa!"))
	if numero%2 == 0:
		print("Número par")
	else:
		print("Número ímpar")
print("Programa finalizado!")







horasTrabalhadas = int(input("Qual o número de horas trabalhadas?"))
salarioPorHora = float(input("Qual seu salário?"))
salarioFinal = 0
valorHorasExtras = 0
horasExtras = (horasTrabalhadas - 160)
salarioParcial = 0
if horasTrabalhadas > 160:
	valorHorasExtras = horasExtras * (salarioPorHora*0.5+salarioPorHora)
	salarioParcial = (horasTrabalhadas - horasExtras)* salarioPorHora 
	salarioFinal = salarioParcial + valorHorasExtras
	print(round(salarioFinal,2))
else: 
	salarioFinal = (horasTrabalhadas - horasExtras)*salarioPorHora
	print(round(salarioFinal,2))







custoDeFabrica = float(input("Digite o custo de fábrica de um carro!"))
porcentagemDoDistribuidor = 28/100
impostos = 45/100
CustoFinal = (custoDeFabrica * porcentagemDoDistribuidor + custoDeFabrica ) + (custoDeFabrica * impostos +custoDeFabrica) + custoDeFabrica
print(CustoFinal)




custoDeFabrica = float(input("Digite o custo de fábrica de um carro!"))
porcentagemDoDistribuidor = 28/100
impostos = 45/100
x = custoDeFabrica + (custoDeFabrica*porcentagemDoDistribuidor)
y = custoDeFabrica + (custoDeFabrica*impostos)
CustoFinal = custoDeFabrica + y + x
print(CustoFinal)































