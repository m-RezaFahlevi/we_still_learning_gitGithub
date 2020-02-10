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
    def __init__(self):
        self.tail = None

    def __append__(self, data):
        #Encapsulate the data in Node
        nodes = Node(data)

        if self.tail == None:
            self.tail = nodes
        else:
            temp = self.tail
            while temp.next:
                temp = temp.next
            temp.next = nodes

words = SinglyLinkedList()
words.__append__("bidoof")
words.__append__("bibarel")
words.__append__("peanut_butter")

#print the data
temps = words.tail
while temps:
    print(f"{temps.data} --> ", end="")
    temps = temps.next
print(None)

#print the address
temps = words.tail
while temps:
    print(f"{hex(id(temps))} -->", end="")
    temps = temps.next
print(None)

print("\nLinked list only using Node class\n")

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
