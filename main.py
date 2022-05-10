from config import ShowMenu
from os import system
from time import sleep

opcao = 0

opcao = ShowMenu(opcao)

while opcao != 0:
  #system('clear') or None
  if opcao == 1:
    exec(open("lancando_dados.py").read())

  elif opcao == 2:
    exec(open("sete_ou_onze.py").read())

  elif opcao == 3:
    exec(open("ped_pap_tes.py").read())
  
  elif opcao == 0:
    break

  else:
    print('\nOpcao Inválida, tente novamente!\n')

  print("\nAguarde 10 segundos para continuar!")
  sleep(10)
  system('clear') or None
  
  opcao = ShowMenu(opcao)
  
  
print("""

      
      ####### O programador agradece por utilizar! #######
              By: Anderson Azevedo da Silva
      """)