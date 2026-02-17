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

# %%Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

# 	O número x é impar
# ou
# 	O número x é par


numero = input ('insira seu numero')
numero = int(numero)

if numero % 2 == 0: 
    print (numero, 'é par')
elif numero % 2 != 0: 
    print (numero, 'é impar')
else: 
    print('insira um numero valido')

#%% Escreva um programa que solicite ao usuário 
# um nome e uma idade,
# e crie um dicionário com essas informações. 
# Em seguida, exiba o dicionário.

nome = input ('insira seu nome')
idade = input ('insira sua idade')

NomeIdade = {nome:idade}

print (NomeIdade)

# %% Faça um programa que receba 4 notas de um aluno. 
# Retorne a média dessas notas, a menor e a maior nota:

Notas = []
count = 4

while count > 0: 
    nota = input ('insira aqui sua nota')
    nota = int(nota)
    Notas.append(nota)
    count -= 1

print('Media Notas', '=', sum(Notas) / len(Notas))
print('Max Notas', '=', max(Notas)) 
print('Min Notas', '=', min(Notas)) 





# %% Considere a lista: [120, “Python”, 120.01, “asw”, False, [10,20] ]

# Faça um programa que retorne as seguintes informações:
# Elemento na posição -1 da lista
# Elemento na primeira posição da lista
# O último caractere do segundo elemento da lista

# Elemento -1: x
# Primeiro elemento: y
# Último caractere do segundo elemento: z

lista =  [120, 'Python', 120.01, 'as', False, [10,20] ]


print ('elemento [-1] = ', lista [-1])

print ('elemento [-1] = ', lista [1])

print ('ultimo',lista [1][-1])


# %% 

# Escreva um programa que solicite ao 
# usuário duas strings e as concatene 
# em uma única String. Em seguida, exiba a String resultante.


isso  = input ('insira um valor') 
aquilo = input ('insira outro valor') 

print (isso + aquilo)



# %% Faça um programa que receba um número. V
# Verifique se este número é primo ou não,
# e retorne o resultado:

n = int (input('Insira um numero: ') )

divisores = 0 

for i in range (1,n + 1):
    if n % i == 0: 
        divisores = divisores + 1

if divisores == 2:
    print ('o numero', n, 'eh primo')
else: 
    print ('o numero', n, 'nao eh primo')


# %% Faça um programa que receba um número. 
# Este número corresponde a uma posição na sequência 
# de Fibonacci: 1, 1, 2, 3, 5,...
# Exiba o número da sequência cuja posição foi informada:
# 	A posição x corresponde ao número y

n = int (input ('insira um numero na sequencia fibonacci'))
lfib = [1,1]

for i in range (2,n): 

    fib = lfib [i-1] + lfib [i-2]
    lfib.append(fib)

print('a posicao', n, 'corresponde ao numero', lfib[n - 1])


# %%Faça um programa com uma função que recebe uma frase.
# Para cada palavra nesta frase, inverta a ordem das letras.
# Exiba o resultado:

frase = input ('insira uma frase: ')

lista = frase.split ()

resultado = []

for palavra in lista: 
    resultado.append (palavra[:: -1])

print (' '.join(resultado))




# %%

# Escreva um programa que exiba os números de 1 a 100. 
# Caso o número seja divisível por 3, exiba “Fizz” no seu lugar, 
# e para múltiplos de 5 exiba “Buzz”. 
# Caso seja divisível por ambos, exiba “FizzBuzz”.



for i in range(1,101):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0: 
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else: 
        print (i)

# %% Faça um programa que receba um número e exiba seu fatorial.

n = int(input ('insira um numero'))
fact = 1

for i in range (1,n+1): 
    fact = fact * i

print (fact)



# %%Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne a posição do menor 
# e do maior valor encontrado:
# O maior valor está na posição x
# O menor valor está na posição y

lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

for x,y in enumerate(lista): 
    if y == max (lista):
        print(x)
    if y == min (lista):
        print(x)

# melhor forma: 

print ('o maior valor está na posição', lista.index(max(lista)))
print ('o menor valor está na posição', lista.index(min(lista)))


# %% Escreva um programa que solicite ao usuário
# um número e exiba a tabuada desse número de 1 a 10.

n = input ('insira um numero pra exibir a tabuada')
n = int(n)
for i in range (1,11): 
    a = n * i
    print (n, '*', i, '=',a)
    

#%% Escreva um programa que solicite ao usuário
# uma palavra e verifique se a palavra é um 
# palíndromo
# (ou seja, é a mesma palavra quando lida de trás para frente).

palavra = input ('insira uma palavra pra checar se ela é um palíndromo: ')

if palavra[::-1] == palavra: 
    print (palavra[::-1]) 
    print (palavra) 
    print('sua palavra é um palíndromo')
else: 
    print (palavra[::-1])
    print (palavra) 
    print('sua palavra nao é um palíndromo')

#%% Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, ele pode apenas apertar 
# o “enter”. Seu programa deve apresentar cada frase 
# e quantas vezes ela foi repetida


