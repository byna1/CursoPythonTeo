#%% faça um programa que receba 4 alturas usando um laço de repeticao e realize a soma desas alturas

soma = 0 # valor final

i = 4 # contador de entradas
 
while i > 0:
   altura = input ('insira uma altura')
   altura = float(altura)
   soma = soma + altura # isso é igual a soma =+ altura
   i = i - 1 # isso é igual a i -= i 
print ('Soma das alturas',soma) 


# %% Faça um programa que receba uma
# quantidade indefinida de valores correspondentes a 
# saldo em conta
# mas quando o usuario aperta enter
# sem digitar valor algum, o programa para de receber valores
# e exibe a soma de todos os valores digitados anteriormente


saldo = 0 

while True: 
    valor = input ('insira o valor pago')
    if valor == "":
        break 

    saldo += float(valor)  

print (saldo)


