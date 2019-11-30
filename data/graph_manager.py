import networkx as nx
from math import sqrt
class GraphManager():
    
    def read_from_file(self, nodes, links):
        graph = nx.Graph()
        with open(nodes, "r") as nodes_file:
            for line in nodes_file.readlines()[1:-1]:
                words = line.split()
                graph.add_node(words[0], x=float(words[2]), y=float(words[3]))
        
        with open(links, "r") as links_file:
            for line in links_file.readlines()[1:-1]:
                link = line.split()
                node_x = link[2] # city 1
                node_y = link[3] # city 2
                
                graph.add_edge(node_x, node_y, weight = self.distance(graph.nodes[node_x], graph.nodes[node_y]))
                

        return graph


    # x - node X of graph
    # y - node Y of graph
    def distance(self, x, y):
        ax = x["x"]
        ay = x["y"]
        bx = y["x"]
        by = y["y"]
        return sqrt((ax-bx)**2 + (ay-by)**2)

    def positions(self, graph):
        posistion_dict = {}

        for node in graph.nodes:
            x = graph.nodes[node]["x"]
            y = graph.nodes[node]["y"]
            posistion_dict[node] = (x,y)
            
        return posistion_dict

    def nodes_path_to_edges(self, path):
        edges_path = []
        if len(path) == 0:
            return []
        prev = path[0]
        for node in path[1:]:
            edges_path.append((prev, node))
            prev = node
        return edges_path





