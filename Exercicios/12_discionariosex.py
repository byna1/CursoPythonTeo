# %% Escreva um programa que crie um dicionario com
# nomes de frutas como chaves e seus
# respectivos precos como valores. 
# Solicite ao usuario o nome de uma fruta
# e exiba o preco correspondente 

Frutas = {
'Maçã': 'R$1,50',
'Banana':'R$2,75',
'Uva': 'R$1,90',
'Pera': 'R$1,25',
'Laranja': 'R$0,65',
'Limão': 'R$1,25',
'Goiaba': 'R$2,15',
'Abacaxi': 'R$3,20',
'Jaca': 'R$5,80'

}

# minha forma 

items = Frutas.items()
Fruta = input('insira o nome da fruta que voce deseja')

for fruta,preco in items: 
    if Fruta == fruta:
        print (preco)

# outra forma 


if Fruta in Frutas:
    print (Frutas[Fruta])
else: 
    print ('insira um valor valido')





#%%

Dicionario = {}

while True:
    NomeFruta = input ('Insira o nome da fruta')
    PrecoFruta = input ('Insira o valor da fruta')
    if NomeFruta == '' or PrecoFruta == '':
        break
    Dicionario [NomeFruta] = PrecoFruta

print (Dicionario)  

# %% Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, 
# ele pode apenas apertar o “enter”.
# Seu programa deve apresentar cada frase 
# e quantas vezes ela foi repetida.

frases = {}

while True: 
    frase =  input ('insira frase')
    if frase == '': 
        break

    if frase not in frases: 
        frases [frase] = 1
    else: 
        frases[frase] += 1

for chave,valor in frases.items():
    print (chave,'->', valor)

# %%
