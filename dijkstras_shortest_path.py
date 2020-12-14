from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 
        
    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)

''' TO DO: Find the shortest path from the source node to every other node in the given graph '''
def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = dict()
    unvisited = graph.nodes
    unvisited.remove(source)
    result[source] = 0

    for value in unvisited:
        result[value] = float('inf')

    path = dict()

    # As long as unvisited is non-empty
    while unvisited: 
        # 1. Find the unvisited node having smallest known distance 
        # from the source node.
        shortest = float('inf')
        node = unvisited.pop()
        if source in graph.neighbours[node]:
            dist = graph.distances[(source, node)]
            if(dist < shortest):
                shortest = dist
                path[source] = node
            result[node] = dist
        else:
            cur_node = node
            sum = 0
            while source not in graph.neighbours[cur_node]:
                for n in graph.neighbours[cur_node]:
                    if graph.distances[(cur_node, n)] < shortest:
                        shortest = graph.distances[(cur_node, n)]
                        shortest_node = n
                # print('NODE', str(cur_node))
                # print('SHORTEST', str(shortest_node))
                cur_node = shortest_node
                sum += shortest + graph.distances[(source, shortest_node)]
                # print(source in graph.neighbours[cur_node], sum)
            result[node] = sum
        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        
        # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.        

        # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    
        # 5. Remove the current node from the unvisited set.

    return result

# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

# print(dijkstra(testGraph, 'A') ==  {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4})

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)
    
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

# print(dijkstra(graph, 'A'))        # {'A': 0, 'C': 10, 'B': 5}
# if dijkstra(graph, 'A') ==  {'A': 0, 'C': 10, 'B': 5}:
#     print('Pass')

# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)
    
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

print(dijkstra(graph, 'A'))
# print(dijkstra(graph, 'A') == {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6})