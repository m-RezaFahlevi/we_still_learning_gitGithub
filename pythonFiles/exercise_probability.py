#Excercise 2.5

dice = [1, 2, 3, 4, 5, 6]
coin = ['H', 'T']
st_S = []
nd_S = []


[[[[st_S.append([i,j,k]) for k in coin] for j in coin] for i in dice if i%2 != 0]]
[[[nd_S.append([i,j]) for j in coin] for i in dice if i%2 == 0]]

for i in st_S: print(i)
print("")
for j in nd_S: print(j)
print("")

S = []

S.extend(st_S)
S.extend(nd_S)

print([i for i in S])
print(f'Length of S : {len(S)}')

S.sort(key=lambda s: s[0])

print(S, end="\n\n")

#Excersice 2.9

#Event A
print("List the elements corresponding to the event that a number less than 3 occurs on the die: ")
print([i for i in S if i[0] < 3], end="\n\n")

#Event B
print("List the elements corresponding to the event that 2 tails occur:")
print([i for i in st_S if i[1] == 'T' and i[2] == 'T'], end="\n\n")

print("List the elements corresponding to the event A-complement: ")
print([i for i in S if i[0] > 3], end="\n\n")

print("List the elements corresponding to the event intersection of A-complement with B: ")
print([i for i in st_S if i[0] > 3 and i[1] == 'T' and i[2] == 'T'], end="\n\n")

print("List the elements corresponding to the event union of A with B: ")
print([i for i in st_S if i[0] < 3 or (i[1] == 'T' and i[2] == 'T')])
