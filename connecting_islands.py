import heapq


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the 
    problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all 
    islands
    """
    total_cost = 0
    graph = []
    # empty list for 0 position
    graph.append([])
    # setting up graph
    for i in range(1, num_islands + 1):
        bridges = []
        for bridge in bridge_config:
            if(i in bridge[:2]):
                target_index = bridge.index(i)
                if target_index == 0:
                    bridges.append(tuple(reversed(bridge[1:])))
                else:
                    bridges.append((bridge[2], bridge[0]))
        graph.append(bridges)
    # print('GRAPH', str(graph))
    minHeap = list()

    # for g in graph:
    #     heapq.heappush(minHeap, g)
    heapq.heappush(minHeap, graph[1])
    print(minHeap)
    return total_cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6
print(get_minimum_cost_of_connecting(num_islands, bridge_config))
test_case = [num_islands, bridge_config, solution]
# test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
# test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
# test_function(test_case)
