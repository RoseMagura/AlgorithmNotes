from collections import defaultdict
import math

class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.neighbours = defaultdict(list)
        # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        # lets make the graph undirected / bidirectional
        self.distances[(to_node, from_node)] = distance

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)


def udacity_dijkstra(graph, start_node, end_node):
    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value 
    # Assume the initial distance to all nodes is infinity.
    # Use math.inf as a predefined constant equal to positive infinity 
    distance_dict = {node: math.inf for node in graph.nodes}
    
    
    # Build a dictionary that will store the "shortest" distance to all nodes, wrt the start_node
    shortest_distance = {}

    distance_dict[start_node] = 0
    
    while distance_dict:
        
        # Sort the distance_dict, and pick the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        print(current_node, node_distance)
        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)

        # Check for each neighbour of current_node, if the distance_to_neighbour is smaller than the alreday stored distance, update the distance_dict
        for edge in current_node.edges:
            if edge.node in distance_dict:
                
                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour
    
    return shortest_distance[end_node]

def traverse(start, end, options):
    all_totals = []
    total = 0
    options.remove(start)
    while start is not end:
        distances = find_distances(start, end, options)
        upcoming = []
        upcoming.append(distances[0])
        min = distances[0][1]
        distances.remove(upcoming[0])
        for item in distances:
            if item[1] == min:
                upcoming.append(item)
        if len(upcoming) > 1:
            for u in upcoming[1:]:
                start = u[0]
                sub_total = 0
                sub_total += u[1]
                while start is not end:
                    options.remove(start)
                    sub_dist = find_distances(start, end, options)
                    start = sub_dist[0][0]
                    sub_total += sub_dist[0][1]
                all_totals.append(sub_total)
        start = upcoming[0][0]
        total += upcoming[0][1]
        if upcoming[0][0] in options:
            options.remove(upcoming[0][0])
    all_totals.append(total)
    return all_totals


def find_distances(start, end, options):
    distances = list()
    for n in graph.neighbours[start]:
        if n in options:
            distances.append((n, graph.distances[(start, n)]))
    distances.sort(key=lambda x: x[1])
    return distances


''' TO DO: Find the shortest path from the source node to every other node in the given graph '''


def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = dict()
    unvisited = set()
    for value in graph.nodes:
        unvisited.add(value)
    path = dict()

    unvisited.remove(source)
    result[source] = 0

    options = graph.nodes
    for value in unvisited:
        result[value] = float('inf')

    shortest = float('inf')

    while unvisited:
        options = ['A', 'B', 'C', 'D', 'E', 'F']
        node = unvisited.pop()
        # find most direct path to source
        if source in graph.neighbours[node]:
            dist = graph.distances[(source, node)]
            if(dist < shortest):
                shortest = dist
                path[source] = node
            result[node] = dist
        cur_node = node
        sum = 0
        indirect = traverse(node, source, options)
        for i in indirect:
            if i < result[node]:
                result[node] = i
    return result


# Test 1
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    graph.add_node(node)

graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'E', 6)
graph.add_edge('B', 'C', 1)
graph.add_edge('C', 'E', 2)
graph.add_edge('E', 'D', 1)

# print(
#     udacity_dijkstra(graph, graph.nodes.get('A'), graph.nodes.get('E')))
    # == {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}):
    # print('Pass')

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

# print(dijkstra(graph, 'A'))        # {'A': 0, 'C': 10, 'B': 5}
if dijkstra(graph, 'A') == {'A': 0, 'C': 10, 'B': 5}:
    print('Pass')

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

if(dijkstra(graph, 'A') == {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}):
    print('Pass')
else:
    print('Fail')
