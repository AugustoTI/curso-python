# Escreva um programa que receba a nota de um aluno (0-10)
# Caso a nota esteja fora desse intervalo peça digitar novamente

nota = int(input('Digite a nota do aluno (0-10): '))

while nota < 0 and nota > 10:
  nota = int(input('Por favor, digite um número que esteja no intervalo de 0 a 10: '))

