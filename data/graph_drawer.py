import networkx as nx
import matplotlib.pyplot as plt 
from data.graph_manager import GraphManager
class GraphDrawer():

    manager = GraphManager()

    def draw(self, graph):
        positions = self.manager.positions(graph)
        nx.draw_networkx(graph, pos = positions)
        plt.show()

    def draw_with_path(self, graph, edges):
        positions = self.manager.positions(graph)
        nx.draw_networkx(graph, pos = positions)
        nx.draw_networkx_edges(graph, pos=positions, edgelist=edges, edge_color="red")
        plt.show()