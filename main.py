from pygraph.classes.undirected_graph import UndirectedGraph
from pygraph.functions.searching.depth_first_search import depth_first_search

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

    #for v in graph.neighbors(2) : print(graph.nodes[v]['id'])
    dfs(graph, 1)

def dfs(graph, start):
    visited[start] = 1
    for v in graph.neighbors(start):
        if visited[graph.nodes[v]['id']] == 0: dfs(graph, graph.nodes[v]['id'])

    print(start)

if __name__ == '__main__':
    main()