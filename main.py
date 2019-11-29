import networkx as net
from data.graph_manager import GraphManager
import matplotlib.pyplot as plt
from algorithms.brute_force import BruteForce
from algorithms.a_star import Astar
from heapq import *
visited = 10 * [0]


def main():
    manager = GraphManager()
    graph = manager.read_from_file("data/examples/poland_nodes.txt", "data/examples/poland_links.txt")

   # graph = net.Graph()
    # for i in range(1, 5): graph.add_node(i)
    # graph.add_edge(1, 2, weight = 1)
    # graph.add_edge(1, 3, weight = 2)
    # graph.add_edge(2, 3, weight = 1)
    # graph.add_edge(2, 4, weight = 3)
    # graph.add_edge(3, 4, weight = 2)

    #print(list(graph.neighbors(1)))
   # print(graph.get_edge_data(1, 2)['weight'])







    # graph.add_edge("1test", "2test", weight = 1)
    # graph.add_edge("2test", "3test", weight = 1)
    # graph.add_edge("3test", "4test", weight = 1)
    # graph.add_edge("1test", "4test", weight = 100)


    BruteForce().run(graph, "Gdansk")
    #BruteForce().run(graph, "1test")
    # Astar().generate_search_space(graph, 1)
    Astar().solve(graph, "Gdansk")
    #Astar().solve(graph, "1test")
    # net.draw_networkx(graph, pos=d)
    # plt.show()
    #l = sorted(list(graph.get_all_edge_objects()), key = lambda x : x['cost'])
    #print(l[0]['vertices'][0])


    #Astar().run(graph, 1)



if __name__ == '__main__':
    main()
