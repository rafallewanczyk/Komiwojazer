import networkx as net
from data.graph_manager import GraphManager
from data.graph_drawer import GraphDrawer
import matplotlib.pyplot as plt
from algorithms.brute_force import BruteForce
from algorithms.a_star import Astar

def main():
    manager = GraphManager()
    drawer = GraphDrawer()
    graph = manager.read_from_file("data/examples/norway_nodes.txt", "data/examples/norway_links.txt")

    BruteForce().run(graph, "N22")
    Astar().solve(graph, "N22")
    

if __name__ == '__main__':
    main()
