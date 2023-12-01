# Receba 4 notas de um aluno e exiba se ele foi:
  # aprovado (nota maior ou igual que 6)
  # ficou de recuperação (nota maior ou igual que 4)
  # reprovado (nota menor do que 4)

nota_1 = float(input('Digite a nota da primeira avaliação: '))
nota_2 = float(input('Digite a nota da segunda avaliação: '))
nota_3 = float(input('Digite a nota da terceira avaliação: '))
nota_4 = float(input('Digite a nota da quarta avaliação: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 6:
  print(f'Aprovado com a média de: {media}')
elif media >= 4:
  print(f'Recuperação pois sua média é de: {media}')
else:
  print(f'Reprovado. Sua média foi de {media}')
