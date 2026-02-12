# escreva um programa que receba uma lista de numeros 
# de usuario e conte quantas vezes um numero especifico 
# aparece na lista

# %% 
lista = [1,2,3,3,3,3,5,1,1,1,1,1,5,6,7,8,1,2,4,5,3]

numero = input ('Entre com um numero')

numero = int(numero)

contador = 0 

for i in lista:
    if i == numero: 
        contador += 1

print ('Quantidade de', numero, ':', contador)

