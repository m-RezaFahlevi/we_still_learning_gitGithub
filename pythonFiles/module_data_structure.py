from collections import deque

deck = deque('abc') #create deque(['a','b','c'])

deck.append('d') #add values d to the right
print(deck)
deck.appendleft('z') #add values z to the left
print(deck)
deck.extend('efg') #add values e, f, g to the right
print(deck)
deck.extendleft('yxw') #add values y, x, w to the left
print(deck, end="\n\n")

deck.pop()
print(deck)
deck.popleft()
print(deck)