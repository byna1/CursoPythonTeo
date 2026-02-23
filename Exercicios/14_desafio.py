#%% 
#  Construa um programa que realiza o sorteio de um 
# # número entre 1 e 15.

# O usuário terá 3 chances de acertar o valor.

# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.

# Caso o usuário acerte, dê os parabéns.

import random

def get_input ():
      while True: 
        try: 
            numero_usuario = int(input('Entre com um numero:'))
        except ValueError as err: 
            print ('entre com um número válido')
            continue
        if 1 <= numero_usuario <=15: 
            return numero_usuario
        print ('Valor invalido! O valor deve ser entre 1 e 15')

numero_sorteio = random.randint(1,15)

for i in range (1,4):

    numero_usuario = get_input()

    if numero_sorteio == numero_usuario: 
        print ('parabens! seu numero esta certo!')
        break

    elif numero_usuario > numero_sorteio: 

        print ('numero muito alto, tente um numero menor')
    else: 

        print ('numero muito baixo, tente um numero maior!')

else: 
    print('suas tentativas acabaram!')




