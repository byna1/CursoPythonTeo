#%%

lista = [1,2,3,4,5,6,7,8,9,10]

for i in lista: 
    if i % 2 == 0: 
        print (i)


#%% 7. Peça ao usuário palavras em um loop (até ele digitar "sair") 
# e no final exiba quantas palavras foram digitadas e quais eram.

listaP = []

while True: 
   palavra =  input ('''
                     Insira uma palavra
                     Para sair digite "sair" ''')
   if palavra != 'sair':
      listaP.append(palavra)
   if palavra == 'sair': 
       break
for y in listaP: 
    print (y)
print ('você inseriu um total de', len(listaP), 'palavras')


#%% 8. Crie um sistema de cadastro de alunos usando dicionário. 
# O usuário pode adicionar alunos com nome e nota, 
# e o programa exibe ao final a média da turma e quem passou (nota >= 6).

NomesNotas = {}

while True:
    nome = input ('insira o nome do aluno ou clique enter para sair')
    if nome == '': 
        break
    nota = input ('insira a nota do aluno')
    nota = float (nota)
    NomesNotas [nome] = nota

valores = list(NomesNotas.values())

print ('a media da turma foi de: ', round(sum(valores)/ len(valores),2))

for y,z in NomesNotas.items():
    if z >= 6:
        print (y, "->", z)

#%% 9. Dada a string "hello world",
# inverta cada palavra separadamente sem usar [::-1]
# direto na string. Resultado esperado: "olleh dlrow".

#%% 1

string = 'hello world'
split = string.split()
nome = ''
nome2 = ''

for i in split[0]: 
    nome = i + nome

for i in split[1]: 
    nome2 = i + nome2

print (nome, '', nome2)

#%% 2

# 1. pede uma frase pro usuário
frase = input('insira uma frase: ')

# 2. divide a frase em palavras separadas
palavras = frase.split(' ')

# 3. cria uma lista vazia pra guardar as palavras invertidas
palavras_invertidas = []

# 4. percorre cada palavra da lista
for palavra in palavras:

    # 5. inverte a palavra e transforma em string de volta
    invertida = ''.join(reversed(palavra))

    # 6. adiciona a palavra invertida na lista
    palavras_invertidas.append(invertida)

# 7. junta tudo com espaço e printa
print(' '.join(palavras_invertidas))


#%% 10. Faça uma matriz 3x3 (lista de listas) preenchida pelo usuário
#e exiba a soma de cada linha, cada coluna e as duas diagonais.


lista = []

for i in range (1,4): 
   A = input ('insira 3 numeros para a coluna a')
   B = input ('insira 3 numeros para a coluna b')
   C = input ('insira 3 numeros para a coluna c')

   A = A.split(' ')
   B = B.split(' ')
   C = C.split(' ')

   lista = lista.append(A)
   lista = lista.append(B)
   lista = lista.append(C)

print (lista)   


# ??????????????????????????
