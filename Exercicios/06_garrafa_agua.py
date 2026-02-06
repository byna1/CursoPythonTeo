# Faça um programa que vende uma garrafa de água: 
# Se o cliente escolher água mineral, será cobrado 1,50
# Se o cliente escolher água mineral com gás, será cobrado 2,50
# %%



texto = """

Escolha a sua água para comprar

(1) Água mineral natural 
(2) Água mineral com gás


"""


opcao = input (texto)

if opcao == '1': 
    print ("Sua conta deu R$ 1,50")
elif opcao == '2':
     print ("Sua conta deu: R$ 2,50")

else: 
    print ('Entre com a porra da opção correta, por favor!')

# %% Altere o programa anterior pra considerar a quantidade de água

''

texto = """

Escolha a sua água para comprar

(1) Água mineral natural 
(2) Água mineral com gás


"""


opcao = input (texto)

valor_item = 0

if opcao == '1': 
    valor_item = 1
elif opcao == '2':
    valor_item = 2.5

if valor_item == 0:
    print ('Entre com a porra da opção correta, por favor!')

else:
    qtde = input ('Quantas garrafas? ')

    valor_total = valor_item * int(qtde)

    print ('Sua conta deu', valor_total)