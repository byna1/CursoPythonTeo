# %%

dadosBarbara = {"nome": 'Bárbara', 
                "idade":"30",
                "formacao": 
                ['psicologa', 'gerencia de projeto e gestao agil'],
                
                'cargos':[
                
                {'empresa':"tj", 'cargo':'conciliadora'},
                {'empresa':'huab', 'cargo':'psicologa hospitalar'},
                {'empresa':'tcs', 'cargo': 'patient safety associate'}
                
                ]
                }

print(dadosBarbara)


# Acessando a chave

dadosBarbara ['nome']

# Acessando um elemento da lista de um dicionario

dadosBarbara['formacao'][1]

# Acessando um elemento dentro de um dicionario que esta num dicionario

print (dadosBarbara['cargos'][-1]['cargo'])


# Criando uma chave nova

dadosBarbara ['estado civil'] = 'casada'


# percorrendo um dicionario com o for

for i in dadosBarbara: 
    print (i, "->", dadosBarbara[i])


# usando o .items
for [chave,valor] in dadosBarbara.items(): 
    print (chave,'->',valor)
    

 