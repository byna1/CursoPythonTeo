
#%%

idades = [17,18,23,4,56,56]

print (idades)

idades.append(32)

print (idades)



#%%


idades = []

while True: 
    idade = input('entre com a sua idade:')
    if idade == "":
        break
    idades.append(int(idade))

print (idades)



