#Create Node Class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(data)
    
    #method for print the list
    def __printlistforwards__(self):
        temp = self
        while(temp):
            print(f'{temp.data} --> ', end="")
            temp = temp.next
        print(None)

    def __printlistbackwards__(self):
        temp = self
        while(temp):
            print(f'{temp.data} --> ', end="")
            temp = temp.previous
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
st_node.__printlistforwards__()
thrd_node.__printlistbackwards__()
