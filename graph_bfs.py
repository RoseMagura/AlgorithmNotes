class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

def bfs_search(root_node, search_value):
    visited = set()
    queue = []
    if root_node.value == search_value:
        return root_node
    else:
        visited.add(root_node)
    current_node = root_node

    for child in current_node.children:
        if len(queue) == 0:
            queue.append(child)
        queue[-1] = child
        visited.add(child)
        if child.value == search_value:
            return child
    while len(queue) > 0:
        current_node = queue[0]
        print(current_node.value)
        for child in current_node.children:
            if len(queue) == 0:
                queue.append(child)
            queue[-1] = child
            visited.add(child)
            if child.value == search_value:
                return child
        queue = queue[1:]

assert nodeA == bfs_search(nodeS, 'A')
# assert nodeS == bfs_search(nodeP, 'S')
# assert nodeR == bfs_search(nodeH, 'R')