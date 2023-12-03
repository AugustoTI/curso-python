# Defina um usuário e senha, em seguida, verifique se o Login é valido.

name = input('Digite seu nome: ')
password = input('Digite sua senha: ')

name_auth = input('Agora digite seu nome novamente para prosseguir com o Login: ')
password_auth = input('Sua senha cadastrada: ')

while name_auth != name or password_auth != password:
  print('Usuário ou senha incorretos. Tente novamente')
  name_auth = input('Seu usuário cadastrado: ')
  password_auth = input('Sua senha cadastrada: ')

print('Login feito com sucesso')
