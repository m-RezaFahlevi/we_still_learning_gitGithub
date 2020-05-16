import numpy as np
from numpy import random

#Initialization
N = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
SIGMA = ['T','W','O','F','U','R']
epochs = 100000

def permutation(domain_set):
    while len(domain_set) != len(SIGMA):
        choosen_number = random.choice(N)
        if choosen_number not in domain_set:
            domain_set.append(choosen_number)
    return domain_set

def main():
    to_alphabet = dict()
    temp = []

    for i in range(epochs):
        permutation(temp)
        while temp[3] == 0:
            pick_a_number = random.choice(N)
            if pick_a_number not in temp:
                temp[3] = pick_a_number
                
        to_alphabet[temp[0]] = SIGMA[0] #T
        to_alphabet[temp[1]] = SIGMA[1] #W
        to_alphabet[temp[2]] = SIGMA[2] #O
        
        to_alphabet[temp[3]] = SIGMA[3] #F
        to_alphabet[temp[4]] = SIGMA[4] #u
        to_alphabet[temp[5]] = SIGMA[5] #R
        
        e1 = temp[0]*100 + temp[1]*10 + temp[2]
        e2 = temp[0]*100 + temp[1]*10 + temp[2]
        e3 = temp[3]*1000 + temp[2]*100 + temp[4]*10 + temp[5]

        temp = []
        if e1 + e2 == e3:
            print("{}\n{}".format(to_alphabet.keys(), to_alphabet.values()))
            print(e1, end="\n{}\n\n".format(e3))
        to_alphabet = {}
        
if __name__ == "__main__":
    main()
