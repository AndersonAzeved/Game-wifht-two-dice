from random import choice

print('Pedra, Papel e Tesoura')
print('HUMANO X MÁQUINA\n')
humano = input('Escolha PEDRA, PAPEL ou TESOURA: ').lower()

lista = ['pedra', 'papel', 'tesoura']
maquina = choice(lista)

print('\nHumano escolheu %s e a Máquina escolheu %s \nQue comecem os jogos!\n' %(humano,maquina))

if humano == maquina:
  print('Deu empate')
  
elif humano == 'pedra' and maquina == 'tesoura':
  print('Humano venceu')

elif humano == 'pedra' and maquina == 'papel':
  print('Máquina venceu')
  
elif humano == 'tesoura' and maquina == 'papel':
  print('Humano venceu')

elif humano == 'tesoura' and maquina == 'pedra':
  print('Máquina venceu')

elif humano == 'papel' and maquina == 'tesoura':
  print('Máquina venceu')

elif humano == 'papel' and maquina == 'pedra':
  print('Humano venceu')  

else:
  print('Escolha inválida')
