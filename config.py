opcao = 0

def ShowMenu(opcao):
  opcao = int(input("""
----------------------------------------
          JOGO COM DADOS
        
        1 _________ Lançando Dados
        2 _________ Sete ou Onze
        3 _________ Pedra, Papel e Tesoura
        0 _________ Sair

        O que deseja? """))
  print('----------------------------------------')
  return opcao

######## DADOS ##########
dados = [
     """
       _______
      |       |
      |   .   |
      |       |
       -------""",

    
  """
       _______
      | .     |
      |       |
      |     . |
       -------""",

  """
       _______
      | .     |
      |   .   |
      |     . |
       -------""",

  """
       _______
      | .   . |
      |       |
      | .   . |
       -------""",

  """
       _______
      | .   . |
      |   .   |
      | .   . |
       -------""",

  """
       _______
      | .   . |
      | .   . |
      | .   . |
       -------"""]
#########################


def DadosJogador(jog1, jog2):
  if jog1 == 1:
    print(dados[0])

  elif jog1 == 2:
    print(dados[1])

  elif jog1 == 3:
    print(dados[2])

  elif jog1 == 4:
    print(dados[3])

  elif jog1 == 5:
    print(dados[4])
  
  elif jog1 == 6:
    print(dados[5])

  if jog2 == 1:
    print(dados[0])

  elif jog2 == 2:
    print(dados[1])

  elif jog2 == 3:
    print(dados[2])

  elif jog2 == 4:
    print(dados[3])

  elif jog2 == 5:
    print(dados[4])
  
  elif jog2 == 6:
    print(dados[5])


def DadosComputer(comp1, comp2):
  if comp1 == 1:
    print(dados[0])

  elif comp1 == 2:
    print(dados[1])

  elif comp1 == 3:
    print(dados[2])

  elif comp1 == 4:
    print(dados[3])

  elif comp1 == 5:
    print(dados[4])
  
  elif comp1 == 6:
    print(dados[5])

  if comp2 == 1:
    print(dados[0])

  elif comp2 == 2:
    print(dados[1])

  elif comp2 == 3:
    print(dados[2])

  elif comp2 == 4:
    print(dados[3])

  elif comp2 == 5:
    print(dados[4])
  
  elif comp2 == 6:
    print(dados[5])