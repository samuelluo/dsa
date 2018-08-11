
# -------------------------------------------------------------------
def topological_sort_helper(graph, visited, stack, node):
    connections = [i for i in graph[node] if i not in visited]
    if len(connections) == 0:
        stack.append(node)
        visited.append(node)
    else:
        for node in connections:
            topological_sort_helper(graph, visited, stack, node)

def topological_sort(graph):
    visited = []
    stack = []
    while len(stack) != len(graph.keys()):
        unvisited = [i for i in graph.keys() if i not in visited]
        node = unvisited[0]
        topological_sort_helper(graph, visited, stack, node)
    print(stack[::-1])

# -------------------------------------------------------------------
graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['D']
graph['C'] = ['D']
graph['D'] = ['E']
graph['E'] = []
topological_sort(graph)

graph = {}
graph[0] = []
graph[1] = []
graph[2] = [3]
graph[3] = [1]
graph[4] = [0, 1]
graph[5] = [0, 2]
topological_sort(graph)
