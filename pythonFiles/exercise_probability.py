#Excercise 2.5
print("Exercise 2.5", end="\n====================\n\n")

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
print("\nExercise 2.5", end="\n=======================\n\n")

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
print([i for i in st_S if i[0] < 3 or (i[1] == 'T' and i[2] == 'T')], end="\n\n")


#Exercise 2.10

print("\nExercise 2.10", end="\n=============================\n\n")
#Sample are taken from three rivers.
prob = ['F', 'NF']
S = [] #Sample space

[[[[S.append([i,j,k]) for k in prob] for j in prob] for i in prob]]

print("The sample space from three rivers: ")
print([i for i in S], end=f'\nLength of set S: {len(S)}\n\n')

print("List the elements of S corresponding to event that at least two of the rivers are save for fishing:")
for i in S:
    if i[0] != 'NF' and i[1] != 'NF': print(i)
    elif i[0] != 'NF' and i[2] != 'NF': print(i)
    elif i[1] != 'NF' and i[2] != 'NF': print(i)

print("Define the event {FFF, NFF, FFN, NFN}")
print([i for i in S if i[1] == "F"], end="\nThis event occurs if and only if the second rivers is save for fishing (F)\n\n")


#Exercise 2.11
print("\nExercise 2.11", end="\n============================\n\n")
male = ['M1', 'M2']
female = ['F1', 'F2']
applicants = []
applicants.extend(male)
applicants.extend(female)

print(applicants)
print(male)
print(female)

print("List the elements of a sample space S:") #A
print([[(i,j) for j in applicants if j != i] for i in applicants], end="\n\n")

print("List the elements of S corresponding to event A that the position of assistant professor is filled by a male applicant:") #B
print([[(i,j) for j in applicants if j != i] for i in male], end="\n\n")

print("List the elements of S corresponding to event B that exctly 1 of the 2 positions was filled by a male applicant:") #C
print([[(i,j) for j in applicants if j in male or i in male] for i in applicants], end="\n\n")

print("List the elements of S corresponding to event C that neither position was filled by a male applicant:") #D
print([[(i,j) for j in female if j != i] for i in female], end="\n\n")
