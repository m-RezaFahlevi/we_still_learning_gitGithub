#prepare the tools
from collections import deque

#create a dictionary constructor first
graph = dict()

#create an adjacency list for the graph
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['A', 'F']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']

def breadth_first_search(graph, root):
    visited_vertices = list()

    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))

        if len(remaining_elements) > 0:
            for elements in sorted(remaining_elements):
                visited_vertices.append(elements)
                graph_queue.append(elements)
            #end_for()
        #end_if()
    #end_while()

    return visited_vertices
#end_def()

print(breadth_first_search(graph, 'A'))
