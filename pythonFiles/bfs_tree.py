tree = dict()

#initialization
tree['A'] = ['B','C']
tree['B'] = ['D','E']
tree['C'] = ['F','G']
tree['D'] = ['H','I']
tree['E'] = ['J','K']
tree['F'] = ['L','M']
tree['G'] = ['N','O']

print(tree)
print(tree.keys())
print(tree.values())
print(type(tree.keys()))
#looping through values
for i in tree.values(): print(i)
for j in tree.keys(): print(j)

readed_tree = []

print(readed_tree)

i = 1; j = 1
for node, leaf in tree.items():
    print(f'{i}-iteration in node')
    i += 1
    if node not in readed_tree: readed_tree.append(node)
    print(readed_tree)
    for leafs in leaf:
        if leafs not in readed_tree:
            readed_tree.append(leafs)
        print(readed_tree)
    print("\n\n")

print(readed_tree)
readed_tree = set(readed_tree)
print(readed_tree)
