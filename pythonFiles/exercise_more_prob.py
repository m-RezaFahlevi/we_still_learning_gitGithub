# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Exercise 2.12
# $
# \text{Exercise and diet are beong studied as possible sibstitues for medication to lower blood pressure.} \\
# \text{Three groups of subjects wil be used to study the effect of exercise.} \\
# \text{Group one is sedentary while group two is wals and group three swims for 1 hour a day.} \\
# \text{Half of ecah of the three exercise groups will be on a salt-free diet.} \\
# \text{And additional group of subjects will not exercise nor restrict their slat, but will take the standard medication.} \\
# \text{Use Z for sedentary, W for walker, S for swimmer, Y for salt, N for no salt, M for medication and F for medication free.} \\
# $
# 
# $
# \text{(a). Show all of the elements of the sample space S.} \\
# $

# %%
S = ['Z', 'W', 'S', 'Y', 'N', 'M', 'F']
print(S)

# %% [markdown]
# $
# \text{(b). Given that A is the set of nomedicatied subjects and B is the set of walkers, list the elements of A} \cup \text{B.}
# $

# %%
print([i for i in S if i == 'F' or i == 'W'])

# %% [markdown]
# # Exercise 2.14
# 
# $
# \text{if S = } \{ \text{0, 1, 2, 3, 4, 5, 6, 7, 8, 9} \} \text{ and A = } \{ \text{0, 2, 4, 6, 8} \} \text{, B = } \{ \text{1, 3, 5, 7, 9} \} \text{, C = } \{ \text{2, 3, 4, 5} \} \text{, and D = } \{ \text{1, 6, 7} \} \\ \text{list the elements of the sets corresponding to the following events:} \\
# \text{(a). } A \cup C = \{ a \in A \cup b \in C \}
# $
# 

# %%
#Setup set S, A, B, C, and D
S = []; A = []; B = []; C = []; D = [1, 6, 7]
for i in range(0,10): S.append(i)
print(f'S = {S}')

[A.append(i) for i in S if i%2 == 0]
print(f'A = {A}')

[B.append(i) for i in S if i%2 != 0]
print(f'B = {B}')

[C.append(i) for i in range(2,6)]
print(f'C = {C}')

print(f'D = {D}')

# A union B
AB = []
AB.extend(A)
AB.extend(B)
print(f'AB = {AB}')

# %% [markdown]
# $\text{(b). } A \cap B = \varnothing $

# %%
print([i for i in S if i%2 == 0 and i%2 != 0])

# %% [markdown]
# $\text{(c). } C^c = \{ c | c \notin C \}$

# %%
Cc = [] #Set C-complement
[Cc.append(i) for i in S if i not in range(2,6)]
print(Cc)

# %% [markdown]
# $\text{(d). } (C^c \cap D) \cup B = \{(c \notin C \text{ and } d \in D) \text{ or } b \in B \}$

# %%
Cc_nB = [1,6,7]
print(B)

print([1,3,5,6,7,9])

# %% [markdown]
# $\text{(e). } (S \cap C)^c = \varnothing$

# %%


