# %% definir o nome do arquivo


nome_arquivo = "historia.txt"

open_file = open (nome_arquivo)

conteudo = open_file.read()

print (conteudo)

open_file.close()


#%% 

nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file: 
    conteudo = open_file.read()

print(conteudo)



# %% lendo csv

arquivo = '17_data.csv'
with open(arquivo) as open_file:
    lines = open_file.readlines()
for l in lines: 
    print(lines)

# fazendo um dicionários com cvs

dados = dict()
chaves = lines [0].strip('\n').split(';')

for c in chaves: 
    dados [c] = []

#inserindo os valores

for l in lines[1:]:
     valores = l.strip('\n').split(';')

     for i in range (0,len(valores)): 
         
         dados [chaves[i]].append(valores[i])

print (dados)


# %%
