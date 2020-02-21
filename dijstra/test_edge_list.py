from graph_adjacency_list import Graph as AdjacencyGraph
from graph_edge_list import Graph as EdgeGraph
from shortest_path import shortest_path
import sys

from ast import literal_eval

with open("test.txt", 'r') as testfile:
    L = testfile.readlines()
    num_tests_run = 0
    
    for l in L:
        (testname, g, s, t, expected_output)  = l.strip().split(";")
        num_tests_run += 1
        
        # Parse the graph
        edge_graph = EdgeGraph()
        edge_graph.graph =  literal_eval(g)

        # testcase = (g,s,t)
        test_result = str(shortest_path(edge_graph,s,t))

        if test_result == expected_output:
            # print("Passed test with name %s" % testname)
            print(test_result)
            continue
          
        elif test_result != expected_output:
            print("Failed test with name %s" % testname)
            print(test_result)
            print(expected_output)
            break

print("Correctly ran %d tests"%num_tests_run)

