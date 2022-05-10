from random import randint
from config import DadosComputer, DadosJogador

print('...............................................')
print('\t\tLançando')

jog1 = randint(1,6)
jog2 = randint(1,6)
comp1 = randint(1,6)
comp2 = randint(1,6)

jogador = jog1 + jog2
computador = comp1 + comp2

print('')
print('Jogadas do Usuário')

DadosJogador(jog1, jog2)
      
print('')
print('Jogadas do Computador')
print('')

DadosComputer(comp1, comp2)

if jogador > computador:
  print('\nParabéns, o Usuário ganhou com %d pontos!\n' %jogador)
  
elif computador > jogador:
  print('\nParabéns, o Computador ganhou com %d pontos!\n' %computador)

else:
  print('\nDeu empate!')

print('...............................................')