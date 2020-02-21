"""
Created on Wed Oct 23 21:47:37 2019

@author: wenyi
"""

# TODO: Your name - Wenyi Chu, wc625
# TODO: Your Partner's name - Qixin Ding, qd49

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

# An implementation of a weighted, directed graph as an edge list. This means
# that it's represented as a list of tuples, with each tuple representing an
# edge in the graph.
class Graph:
  def __init__(self):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.graph = []

  def add_edge(self, node1, node2, weight):
    # Adds a directed edge from `node1` to `node2` to the graph with weight
    # defined by `weight`.
    if not self.has_edge(node1,node2):
      self.graph.append((node1,node2,weight))

  def has_edge(self, node1, node2):
    # Returns whether the graph contains an edge from `node1` to `node2`.
    # DO NOT EDIT THIS METHOD
    return (node1, node2) in [(x,y) for (x,y,z) in self.graph]

  def get_neighbors(self, node):
    # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    # `x` is the neighbor node, and `y` is the weight of the edge from `node`
    # to `x`.
    return [(node2,weight) for (node1,node2,weight) in self.graph if node1==node]

# print("Testing edge list graph...")
# edge_graph = Graph()
# edge_graph.add_edge('a', 'b', 1) 
# print(edge_graph.get_neighbors('a'))

# # example graph from slides
# edge_graph_2 = Graph()
# edge_graph_2.graph = (('s',9,9), (2,3,24), ('s',6,14),
#   (6,3,18), (6,5,30),
#   (3,5,2),  (5,4,11), (4,3,6),
#   (3,'t',19), (4,'t',6),  (5,'t',16),
#   (7,'t',44), (6,7,5),  ('s',7,15))
# print(edge_graph_2.get_neighbors('s'))
