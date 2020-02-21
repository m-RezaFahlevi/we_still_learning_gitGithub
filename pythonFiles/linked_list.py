#Create Node Class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    #We still have no idea what is this code
    #use for :)
    def __str__(self):
        return str(data)

class SinglyLinkedList:
    #We still have no idea what is
    #self.head and self.tail used for :)

    #Take note of the convention being used. The point at which we append 
    #new nodes is through self.head. 
    #The self.tail variable points to the first node in the list.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Time-complexity is O(n)
    def __appends__(self, data):
        #Encapsulate the data in Node
        nodes = Node(data)

        if self.tail == None:
            self.tail = nodes
        else:
            temp = self.tail
            while temp.next:
                temp = temp.next
            temp.next = nodes

    def __append__(self,data):
        #Encapsulate the data in Node
        node = Node(data)
        self.size += 1      #Reduce the time-complexity
        if self.head:
            self.head.next = node
            self.head = node
        else:
            #This code will execute only in the first __append__ is used.
            self.tail = node
            self.head = node

    def __delete__(self, data):
        temp = self.tail
        prev = self.tail
        while temp:
            if(temp.data == data and temp == self.tail):
                self.tail = temp.next
            else:
                prev.next = temp.next
            self.size -= 1
            return
        prev = temp
        temp = temp.next

    #Time-complexity is O(n)
    def __size__(self):
        temp = 0
        current = self.tail
        while current:
            temp += 1
            current = current.next
        return temp

    #Improving list traversal
    def iter(self):
        temp = self.tail
        while temp:
            val = temp.data
            temp = temp.next
            yield val

"""
    Linked list by using SinglyLinkedList class
    and using encapsulation-technique.
"""

words = SinglyLinkedList()

words.__append__(str(input("Node : ")))
words.__append__(str(input("Node : ")))
words.__append__(str(input("Node : ")))

print("\nYour list : ")

#Access the data
for words in words.iter():
    print(words)

words.__delete__(str(input()))

#print the data
"""
suddenly this code below  become error :)

temps = words.tail
while temps:
    print(f"{temps.data} --> ", end="")
    temps = temps.next
print(None, end="\n")
print(f'\nthe size of linked_list is : {words.size}')

#print the address
print("The address of the list:")
temps = words.tail
while temps:
    print(f"{hex(id(temps))} --> ", end="")
    temps = temps.next
print(None)
"""
#print(hex(id(st_node)))  // This is for display the memory address of variable
