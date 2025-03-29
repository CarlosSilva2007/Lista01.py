#Questão número 1:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_simples = (nota1 + nota2 + nota3) / 3
print(f'Média Aritmética Simples: {media_simples:.2f}')

media_ponderada1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / (2 + 2 + 3)
print(f'Média Ponderada (pesos 2, 2 e 3): {media_ponderada1:.2f}')

media_ponderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / (1 + 2 + 2)
print(f'Média Ponderada (pesos 1, 2 e 2): {media_ponderada2:.2f}')

#Questão número 2:
valor = float(input("Digite o valor total das mercadorias: R$ "))

if valor >= 500:
imposto = (valor - 500) * 0.50
valor_total = valor + imposto
print(f'O imposto é de R$ {imposto:.2f}. O valor total a ser pago é R$ {valor_total:.2f}.')
else:
print(f'Não há imposto. O valor total a ser pago é R$ {valor:.2f}.')

#Questão número 3:
valor = float(input("Digite o valor total das mercadorias: R$ "))

if valor >= 500:
imposto = (valor - 500) * 0.50
valor_total = valor + imposto
print(f'O imposto é de R$ {imposto:.2f}. O valor total a ser pago é R$ {valor_total:.2f}.')
else:
print(f'Não há imposto. O valor total a ser pago é R$ {valor:.2f}.')

#Questão número 4:
dias = int(input("Digite o número de dias de aluguel: "))
km_rodados = float(input("Digite o número de quilômetros rodados: "))

valor_diario = 90 * dias
valor_adicional = 0
if km_rodados > 100:
valor_adicional = (km_rodados - 100) * 12

valor_total = valor_diario + valor_adicional
print(f'O valor total a ser pago é R$ {valor_total:.2f}.')

#Questão número 5:
for i in range(1, 101):
print(i)

#Questão número 6:
def eh_primo(n):
if n <= 1:
return False
for i in range(2, int(n ** 0.5) + 1):
if n % i == 0:
return False
return True

primos = []
n = 2
while len(primos) < 100:
if eh_primo(n):
primos.append(n)
n += 1

print(primos)

#Questão número 7:
numero = int(input("Digite um número ímpar: "))

numero_anterior = numero - 2
numero_proximo = numero + 2

diferenca = (numero_proximo ** 2) - (numero_anterior ** 2)
print(f'A diferença entre os quadrados de {numero_proximo} e {numero_anterior} é {diferenca}.')

#Questão número 8:
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}°F.')

#Questão número 9:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f'O maior número é {maior} e o menor número é {menor}.')

#Questão número 10:
numero = int(input("Digite um número inteiro maior que 1: "))

def eh_primo(n):
if n <= 1:
return False
for i in range(2, int(n ** 0.5) + 1):
if n % i == 0:
return False
return True

if eh_primo(numero):
print(f'{numero} é um número primo.')
else:
print(f'{numero} não é um número primo.')

#Questão número 11:
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == senha:
print("Erro: O nome de usuário não pode ser igual à senha.")
else:
print("Login realizado com sucesso!")

#Questão número 12:
turmas = int(input("Digite a quantidade de turmas: "))
total_alunos = int(input("Digite a quantidade total de alunos: "))

media = total_alunos / turmas
print(f'A média de alunos por turma é {media:.2f}.')

if media > 40:
print("Aviso: Alguma turma tem mais de 40 alunos.")

#Questão número 13:
salario = float(input("Digite o salário inicial: R$ "))
anos = int(input("Digite o número de anos: "))

for i in range(anos):
salario *= 2

print(f'O salário após {anos} anos é R$ {salario:.2f}.')
