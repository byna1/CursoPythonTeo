# %%
A = 1
B = 5


print(A)
print (B)

# %%


C = A

A = B 

B = C 

print (A)
print (B)

# %% 

A,B = B,A

print (A)
print (B)

# %%

nova = A,B


# %%

a,b,*_ = 1,2,3,4,5

print (a,b)

# %% 

def soma (a,*args): 
    total = a * sum(args)
    return total

soma (1,2,4,7)