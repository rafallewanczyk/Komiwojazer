from data.graph_manager import GraphManager
import networkx as nx
import matplotlib.pyplot as plt 

if __name__ == "__main__":
    reader = GraphManager()
    graph = reader.read_from_file("data/examples/poland_nodes.txt", "data/examples/poland_links.txt")
    positions = reader.positions(graph)
    nx.draw_networkx(graph, pos=positions)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edges(graph, pos=positions, edgelist=[("Gdansk","Warsaw"), ("Gdansk", "Kolobrzeg")], edge_color="red")
    plt.show()