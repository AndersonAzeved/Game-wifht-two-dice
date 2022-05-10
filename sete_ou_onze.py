from random import randint
from config import DadosJogador

print('...............................................')
print('\t\tSete ou Onze')

jog1 = randint(1,6)
jog2 = randint(1,6)
soma = jog1 + jog2

print('Jogadas')

DadosJogador(jog1, jog2)

if soma == 7 or soma == 11:
  print('\nParabéns, o Usuário ganhou com %d pontos!\n' %soma)
  
else:
  print('\nParabéns, o Computador ganhou com %d pontos!\n' %soma)

print('...............................................')