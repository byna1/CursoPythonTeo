
# %%

import requests
import json
from tqdm import tqdm
import pandas as pd

ceps = ['0151900', '14400760', '59151590',  
    "01001-000",  # São Paulo - Praça da Sé
    "20040-010",  # Rio de Janeiro - Centro
    "30140-110",  # Belo Horizonte - Centro
    "70040-010",  # Brasília - Esplanada dos Ministérios
    "40020-000",  # Salvador - Centro
    "80010-000",  # Curitiba - Centro
    "90010-150",  # Porto Alegre - Centro Histórico
    "50010-000",  # Recife - Bairro do Recife
    "69005-070",  # Manaus - Centro
    "66017-000"   # Belém - Nazaré
    ]

url = 'https://viacep.com.br/ws/{cep}/json/'
dados = []

for i in tqdm(ceps): 
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

print(dados)

#%% 
dataset = pd.DataFrame(dados)
dataset.to_csv('ceps.csv',sep=';')
dataset

#%% 

with open ('cep.json', 'w',encoding='utf-8') as open_file:
    json.dump(dados,open_file,ensure_ascii=False,indent=4)



