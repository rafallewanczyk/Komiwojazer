from pygraph.classes.undirected_graph import UndirectedGraph
from heapq import *

visited = 10 * [0]


def main():
    print("start")
    graph = UndirectedGraph()

    for i in range(1, 10): graph.new_node()
    graph.new_edge(1, 2, 0)
    graph.new_edge(2, 4, 0)
    graph.new_edge(2, 5, 0)
    graph.new_edge(5, 6, 0)
    graph.new_edge(1, 3, 0)
    graph.new_edge(3, 7, 0)
    graph.new_edge(3, 8, 0)
    graph.new_edge(8, 9, 0)

    heap = []
    heappush(heap, 1)
    heappush(heap, 3)
    heappush(heap, 0)
    heappush(heap, 8)
    print(heap)
    heappop(heap)
    print(heap)

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
