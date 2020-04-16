def open_files(files_name):
    try:
        files = open(files_name)
    except:
        print("File is not found")

    print(type(files))
    count = dict() # count[key] : value
    for line in files:
        words = line.split()
        print(words, end=f'\nlength: {len(words)}\n')
        for word in words:
            print(word, end=f' length : {len(word)}\n')
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    

    #return(count)

print(open_files('scraping_britannica_protocols.txt'))
