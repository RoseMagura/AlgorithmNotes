# counter = 0
#     while unvisited:
#     # while counter < 10:
#         options = unvisited
#         options.add(source)
#         cur_node = unvisited.pop()
#         while cur_node is not source:
#             counter += 1

#             if counter > 10:
#                 break
#             print(cur_node)
#             shortest = float('inf')
#             sum = 0
#             for neighbor in graph.neighbours[cur_node]:
#                 if neighbor in options:
#                     distance = graph.distances.get((cur_node, neighbor), None)
#                     if distance is not None:
#                         if distance < shortest:
#                             shortest = distance
#                             cur_node = neighbor
#                             options.remove(neighbor)
#             sum += shortest
#             print(sum)


#     # u_neighbors = set()
#     # for n in graph.neighbours[shortest_node]:
#     #     if(n in unvisited):
#     #         u_neighbors.add(n)
    
#     # for u in u_neighbors:
#     #     u_dist = graph.distances.get((source, u), None) 
#     #     print(u_dist)
#     #     if(u_dist < shortest):
#     #         print('shorter')
#     #         shortest = u_dist

#     # for node in unvisited:
#     #     dist = graph.distances.get((source, node), None)
#     #     if dist is not None:
#     #         if dist < shortest:
#     #             shortest = dist
#     #             shortest_node = node



# # node = unvisited.pop()
# # if source in graph.neighbours[node]:
# #             dist = graph.distances[(source, node)]
# #             if(dist < shortest):
# #                 shortest = dist
# #                 path[source] = node
# #             result[node] = dist
# #         cur_node = node
# #         sum = 0
# #         while source not in graph.neighbours[cur_node]:
# #             for n in graph.neighbours[cur_node]:
# #                 if graph.distances[(cur_node, n)] < shortest:
# #                     shortest = graph.distances[(cur_node, n)]
# #                     shortest_node = n
# #             # print('NODE', str(cur_node))
# #             # print('SHORTEST', str(shortest_node))
# #             cur_node = shortest_node
# #             sum += shortest + graph.distances[(source, shortest_node)]
# #             # print(source in graph.neighbours[cur_node], sum)
# #             result[node] = sum