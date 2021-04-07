import math

class Edge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class Node(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(Edge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

    def __repr__(self):
        return 'Node({})'.format(self.value)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


node_gateway = Node('gateway')
node_lab = Node('lab')
node_backbone_a = Node('backbone_a')
node_backbone_b = Node('backbone_b')
node_north_building = Node('north_building')
node_east_building = Node('east_building')
node_south_building = Node('south_building')

network_graph = Graph([node_gateway, node_north_building, node_lab, node_east_building, node_south_building, node_backbone_a, node_backbone_b])
network_graph.add_edge(node_gateway, node_lab, 4)
network_graph.add_edge(node_gateway, node_east_building, 6)
network_graph.add_edge(node_gateway, node_north_building, 3)
network_graph.add_edge(node_north_building, node_gateway, 3)
network_graph.add_edge(node_north_building, node_east_building, 4)
network_graph.add_edge(node_lab, node_gateway, 4)
network_graph.add_edge(node_lab, node_south_building, 7)
network_graph.add_edge(node_east_building, node_north_building, 4)
network_graph.add_edge(node_east_building, node_gateway, 6)
network_graph.add_edge(node_east_building, node_south_building, 4)
network_graph.add_edge(node_east_building, node_backbone_a, 5)
network_graph.add_edge(node_south_building, node_lab, 7)
network_graph.add_edge(node_south_building, node_east_building, 4)
network_graph.add_edge(node_south_building, node_backbone_b, 4)
network_graph.add_edge(node_backbone_a, node_east_building, 5)
network_graph.add_edge(node_backbone_a, node_backbone_b, 5)
network_graph.add_edge(node_backbone_b, node_south_building, 4)
network_graph.add_edge(node_backbone_b, node_backbone_a, 5)

def get_lookup_table(network_graph):
    """
    Get a lookup table that contains the shortest path between any two points.

    Parameters
    ----------
    network_graph : Graph
        The computer network graph

    Returns
    -------
    lookup_table : dict of dict
        Lookup table

        Ex.
        If you want to get the shortest path between `node_a` and `node_b`, you would do `lookup_table[node_a][node_b]`.
    """
    lookup_table = dict()
    
    for node in network_graph.nodes:
        lookup_table[node.value] = {}
    
    return lookup_table

lookup_table = get_lookup_table(network_graph)
print(lookup_table)

# print('Shortest Path from {} to {} is {}'.format(
#     node_gateway.value, node_south_building.value, lookup_table[node_gateway][node_south_building]))