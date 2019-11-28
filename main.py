from pygraph import graph_to_dot
from pygraph.classes.undirected_graph import UndirectedGraph
from algorithms.brute_force import BruteForce
from algorithms.a_star import Astar
from algorithms.astar import *
from heapq import *
visited = 10 * [0]


def main():
    graph = UndirectedGraph()

    for i in range(1, 5): graph.new_node()
    graph.new_edge(1, 2, 2)
    graph.new_edge(2, 3, 3)
    graph.new_edge(1, 3, 9)
    graph.new_edge(3, 4, 7)
    #BruteForce().run(graph, 1)
    Astar().generate_search_space(graph, 1)
    #Astar().run(graph, 1)


def dfs(graph, start):
    visited[start] = 1
    for v in graph.neighbors(start):
        if visited[graph.nodes[v]['id']] == 0: dfs(graph, graph.nodes[v]['id'])

    print(start)


def comp(a, b):
    if a > b:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
