# %% Faça um programa que dê bom dia;

print ('Bom dia!')

# %% Faça um programa que de bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela, citando o nome da pessoa.


nome =  input ('Bom dia! Qual é o seu nome?')

print ('É um prazer te conhecer,', nome)


# %% Crie uma história simples.
# Adicione essa história em um programa. 
# A cada parágrafo, a história deve aguardar o usuário apertar “enter” para dar continuidade.


inicio = input ('''Olá, você quer ouvir uma história?
                (1) Sim
                (2) Nao''')
if inicio == '1':
    print('Eu fui a secretaria de saude de courbevoie hoje')
    meio = input ('Clique enter para continuar')
elif inicio == '2':
    print ('Tudo bem, quem sabe na proxima!')
else: 
    print ('Por favor, digite apenas 1 para sim ou 2 para nao')

if meio == '':
    print('precisei entregar meus documentos para fazer meu número de seguridade social')
    fim = input ('Clique enter para continuar')
else: 
    print ('Por favor, digite apenas enter para continuar')
if fim == '':
    print('Isso deve demorar 1 mês pra chegar')
else: 
    print ('Por favor, digite apenas enter para continuar')



# %% Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

input_inteiro = input('Insira um numero inteiro')

raiz_quadrada = int(input_inteiro) ** (1/2)

print (raiz_quadrada)

#%% Faça um programa que exiba o dobro de um número inserido pelo usuário.

input_inteiro = input ('insira um numero inteiro')

dobro = int(input_inteiro) * 2

print (dobro)


# %% Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago



tipo_sorvete = input ('''Escolha o seu tipo de sorvete: 
                      (1) Casquinha (R$1,00), 
                      (2) Cascão (R$2,50), 
                      (3) Cestinha (R$4,00)
                      ''')

if tipo_sorvete == '1':
    valor_tipo = 1.00

elif tipo_sorvete == '2': 
    valor_tipo = 2.50

elif tipo_sorvete == '3': 
    valor_tipo = 4.00

else: 
    print ('Por favor, escolha uma das tres opcoes')



sabor_sorvete = input ('''Escolha o sabor do seu sorvete: 
           
           (1) morango, 
           (2) creme, 
           (3) chocolate''')

cobert_sorv = input ('''Agora escolha a cobertura do sorvete: 
                          (1) Caramelo (R$1,50),
                          (2) morango (R$1,50), 
                          (3) chocolate (R$1,50), 
                          (4) sem cobertura (R$0,00)''')

if   cobert_sorv == '1':
    valor_cobert = 1.50


elif cobert_sorv == '2':
    valor_cobert = 1.50

elif cobert_sorv == '3':
    valor_cobert = 1.50

elif cobert_sorv == '4':
    valor_cobert = 0

else: 

    print ('Por favor, adcione uma das opcoes')


valor_total = valor_tipo + valor_cobert

print ('esse eh o seu valor total',valor_total)


# %%
