# Estruturas de repetição - While

count = 1
while count <= 10:
  print(f'Mensagem do count: {count}')
  count += 1

count2 = 1
while count2 <= 10:
  if count2 == 5:
    break
  if count2 == 6:
    continue
  print(f'Mensagem do count2: {count2}')
  count2 += 1
