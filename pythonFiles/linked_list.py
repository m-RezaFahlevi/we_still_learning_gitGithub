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
