number_integers = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five"}
number_integers[6] = "six"
number_integers.update({7 : "seven", 8 : "eight"})

print(number_integers.items())
print(type(number_integers))
print(1 in number_integers)
print(number_integers, end="\n\n")

print(f"The key of number_integers : {list(number_integers)}")
print(number_integers.values())

print(sorted(list(number_integers)))
print(sorted(list(number_integers.values())))

#sorted dictionary-list respect with the keys
print(sorted(list(number_integers), key=number_integers.__getitem__))

french_integers = {
    'one' : 'uno',
    'two' : 'deux',
    'three' : 'trois',
    'four' : 'quatre',
    'five' : 'cinq',
    'six' : 'six'
}

print([french_integers[i] for i in sorted(french_integers, key=french_integers.__getitem__)])
print(f"\n\n{french_integers}")
print(french_integers.values())
print(sorted(french_integers, key=french_integers.__getitem__))

def word_count(file_name):
    """ 
    create a dictionary with dictionary_name[keys] : values
    where the words in file_name.txt as keys
    and values as the frequency of words
    """
    try:
        file_hand = open(file_name)
    except:
        print('File 404 not found / cannot be opened')
        exit()

    count = dict()
    for line in file_hand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1 #e.g : count["bidoof"] : 1; means bidoof count as 1 if key: words not in count
            else:
                count[word] += 1 #i.e: count["bidoof"] : 1, means count["bidoof"] = (count["bidoof"] := 1) + 1
        #end_for(word)
    #end_for(line)
    print(f'\n{word_count.__doc__}')
    return(count)
#end_def

counts = word_count('some_txt.txt')
filtered = {key:value for key, value in counts.items() if value < 20}
print(filtered, end="\n\n")
print(filtered.items())
