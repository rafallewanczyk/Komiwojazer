import unittest
import networkx as nx
from math import sqrt
from data.graph_manager import GraphManager

class GraphManagerTest(unittest.TestCase):

    graph_manager = GraphManager()

    def test_read_from_file(self):
        graph = self.graph_manager.read_from_file("test/test1_nodes.txt", "test/test1_links.txt")

        self.assertEqual(graph.number_of_nodes(), 4)
        self.assertEqual(graph.number_of_edges(), 4)
        self.assertSetEqual(set(graph.neighbors("A")), {"B"})
        self.assertSetEqual(set(graph.neighbors("B")), {"A", "C", "D"})
        self.assertEqual(graph.get_edge_data("A","B")['weight'], 5)
        self.assertEqual(graph.get_edge_data("B","A")['weight'], 5)

    def test_distance(self):
        graph = self.graph_manager.read_from_file("test/test1_nodes.txt", "test/test1_links.txt")

        self.assertEqual(self.graph_manager.distance(graph.nodes["A"], graph.nodes["B"]), 5)
        self.assertEqual(self.graph_manager.distance(graph.nodes["C"], graph.nodes["D"]), sqrt(13))

    def test_positions(self):
        graph = self.graph_manager.read_from_file("test/test1_nodes.txt", "test/test1_links.txt")
        positions = {
            "A": (0.0, 1.0),
            "B": (3.0, 5.0),
            "C": (6.0, 3.0),
            "D": (4.0, 0.0),
        }
        self.assertDictEqual(self.graph_manager.positions(graph), positions)


if __name__ == "__main__":
    unittest.main()