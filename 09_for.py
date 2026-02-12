#%%
nome = "lulu lindona"

for letra in nome: 
    print (letra)

#%% exemplo da tabuada 

numero = 2 
max_numero = 100

for i in range (1, max_numero + 1): 
    print (numero, 'x', 1, '=', numero * i)


#%% divisiveis por 4

for i in range (4, 101): 
    if i % 4 == 0:
        print (i)




# %% insira altura 4 vezes e some


soma = 0 
qtd_entradas = 4

for i in range(qtd_entradas):
        altura = input ('insira aqui a altura')
        soma = float(soma) + float(altura)
   

print ('esta eh a soma:', soma)

