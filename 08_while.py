numero = 2


print ('2 x 1 =', 2*1)

#%% 
count = 1 
while count <= 10:
    print ('depois', count)
    count =  count + 1

#%% tabuada de 2


numero = 2 
count = 1
while count <= 100: 
    print (numero, "x", count, "=", numero * count )
    count = count + 1

print ('acabou!')



##%% Quais sao todos
# %% os numeros divisiveis por 4 no intervalo de 4 a 100


count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print (count)
    count += 1 
