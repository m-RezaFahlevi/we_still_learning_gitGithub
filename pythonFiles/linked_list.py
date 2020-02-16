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

    #method for print the list
    #if we are only using Node class
    def __print_list_forwards__(self):
        temp = self
        while(temp):
            print(f'{temp.data} --> ', end="")
            temp = temp.next
        print(None)

    def __print_list_backwards__(self):
        temp = self
        while(temp):
            print(f'{temp.data} --> ', end="")
            temp = temp.previous
        print(None)

    def __display_the_address__(self):
        temp = self
        while(temp):
            print(f'{hex(id(temp))} --> ', end="")
            temp = temp.next
        print(None)

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

    #Time-complexity is O(n)
    def __size__(self):
        temp = 0
        current = self.tail
        while current:
            temp += 1
            current = current.next
        return temp

"""
    Linked list by using SinglyLinkedList class
    and using encapsulation-technique.
"""

words = SinglyLinkedList()

words.__append__(str(input("Node : ")))
words.__append__(str(input("Node : ")))
words.__append__(str(input("Node : ")))

print("\nYour list : ")

#print the data
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

print("\nLinked list only using Node class\n")



"""
    Linked list only using the node class.
    I think this method is not too good. Because we need
    to allocate the the node to its memory.
"""
#Allocate the data for each node
st_node = Node("st_data")
nd_node = Node("nd_data")
thrd_node = Node("thrd_data")

#Linked the node
st_node.next = nd_node
nd_node.next = thrd_node
nd_node.previous = st_node
thrd_node.previous = nd_node

#use the method
st_node.__print_list_forwards__()
thrd_node.__print_list_backwards__()
st_node.__display_the_address__()

#Insert new node between the linked_node
new_node = Node("new_data")

nd_node.next = new_node
new_node.previous = nd_node
new_node.next = thrd_node

print("\nAfter insert the new node between linked_node\n")

st_node.__print_list_forwards__()
thrd_node.__print_list_backwards__()
st_node.__display_the_address__()
#print(hex(id(st_node)))  // This is for display the memory address of variable
