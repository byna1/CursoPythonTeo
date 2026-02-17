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


string = 'hello world'
stringsplit = string.split()
lista = []

for i in string: 
    lista = i + lista

print (lista)


#%% 10. Faça uma matriz 3x3 (lista de listas) preenchida pelo usuário
#e exiba a soma de cada linha, cada coluna e as duas diagonais.


Dicionario = {}
a = []
b = []
c = []

for i in range (1,4): 
    a = [a] + [input ('insira numeros')]
    b = [b] + [input ('insura numeros')]
    c = [c] + [input ('insira numeros')]


print (a)



