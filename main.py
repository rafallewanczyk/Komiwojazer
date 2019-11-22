from pygraph.classes.undirected_graph import UndirectedGraph
from algorithms.brute_force import BruteForce
from algorithms.astar import *
from heapq import *
visited = 10 * [0]


def main():
    graph = UndirectedGraph()

    for i in range(1, 8): graph.new_node()
    graph.new_edge(1, 2, 8)
    graph.new_edge(1, 3, 4)
    graph.new_edge(1, 4, 5)
    graph.new_edge(2, 5, 4)
    graph.new_edge(2, 7, 12)
    graph.new_edge(3, 5, 8)
    graph.new_edge(3, 7, 19)
    graph.new_edge(3, 6, 9)
    graph.new_edge(4, 7, 99)
    graph.new_edge(4, 6, 7)
    graph.new_edge(5, 7, 11)
    graph.new_edge(6, 7, 7)

    BruteForce().run(graph, 1)

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
