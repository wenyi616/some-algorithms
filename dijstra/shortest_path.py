"""
Created on Wed Oct 23 21:47:37 2019

@author: wenyi
"""

# TODO: Your name - Wenyi Chu, wc625
# TODO: Your Partner's name - Qixin Ding, qd49

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

def shortest_path(graph, source, target):
  length = -1
  path = []
  prev = {}
  # you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  
  # Create an empty list that keeps track of vertices included in shortest path tree
  explored = []

  # set distance value for other vertices INF (see below)
  # set distance value for the source = 0 (so that it is picked first)
  dist = {}
  dist[source]=0

  while(target not in explored):

    dist_list = list(dist.values())
    dist_key_list = list(dist.keys())

    # reomve explored vertices and their distances from dist_list, to ensure that min is not explored
    for u in explored:
      dist_list.remove(dist[u])
      dist_key_list.remove(u)
    
    # pick minimum dist
    min_dist = min(dist_list)

    # min dist, u cannot be in explored. add u to explored
    u = dist_key_list[dist_list.index(min_dist)]
    explored.append(u)

    # iterate all neighbors (a list of tuple) and update distance if necessary
    neighbors = graph.get_neighbors(u)
    if(neighbors == None):
      continue

    else:
      for neighbor in neighbors:
        v = neighbor[0]
        
        if v in dist:
          d = dist[v]
        else:
          d = float('inf')
        
        d_new = neighbor[1] + dist[u]
        
        if d_new < d:
          # update dist[v]
          dist[v] = d_new
          prev[v] = u

  
  # compute path
  curr = target
  path.insert(0,target)
  while prev[curr] != source:
    path.insert(0,prev[curr])
    curr = prev[curr]
  path.insert(0,source)
  
  # compute path length
  length = dist[target]

  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  return (path,length)



# TEST CASE
from graph_edge_list import Graph as EdgeGraph

# # example graph from slides
# edge_graph = EdgeGraph()
# edge_graph.graph = (('s',9,9), (2,3,24), ('s',6,14),
#   (6,3,18), (6,5,30),
#   (3,5,2),  (5,4,11), (4,3,6),
#   (3,'t',19), (4,'t',6),  (5,'t',16),
#   (7,'t',44), (6,7,5),  ('s',7,15))
# print(shortest_path(edge_graph, 's', 't'))

# edge_graph = EdgeGraph()
# edge_graph.graph = (('A','B',4), ('A','C',3),('C','E',2),('A','E',7),('C','D',3),('D','F',4),('E','F',2))
# print(shortest_path(edge_graph, 'A', 'F'))